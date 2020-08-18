from typing import Union, List, Dict, Callable, Any, Tuple, Optional
import importlib
from collections import defaultdict
from dataclasses import dataclass, field
from dataclass_serializer import Serializable, deserialize

import numpy as np
import pandas as pd

import torch
import torch.nn as nn
from torch.utils.data import DataLoader


from ..metrics import Metric, Metrics
from ..lr_schedulers import LRScheduler
from ..optimizers import Optimizer
from ..losses import Loss
from ..samplers import Sampler
from ..callbacks import Callback, CallbackList, History, ProgbarLogger, LambdaCallback
from ..data import XDataset, XYDataset
from ..seed import set_seed


def dynamic_load(name):
    modname, clfname = name.rsplit(".", 1)
    mod = importlib.import_module(modname)
    return getattr(mod, clfname)


def _to_device(x, device, non_blocking=True):
    if isinstance(x, (list, tuple)):
        return x.__class__([_to_device(xi, device) for xi in x])
    if isinstance(x, dict):
        return {
            k: _to_device(v, device, non_blocking=non_blocking) for k, v in x.items()
        }
    return x.to(device, non_blocking=non_blocking)


class data_prefetcher:
    def __init__(self, loader, device, gpu=-1, prefetch=True):
        self.gpu = gpu
        self.device = device
        self.loader, self.prefetch = loader, prefetch
        if gpu >= 0 and prefetch:
            self.stream = torch.cuda.Stream()

    def preload(self):
        try:
            self._next = next(self.iterator_)
        except StopIteration:
            self._next = None
            return

        with torch.cuda.stream(self.stream):
            self._next = _to_device(self._next, self.device, non_blocking=True)

    def __iter__(self):
        self.iterator_ = iter(self.loader)
        if self.gpu >= 0 and self.prefetch:
            self.preload()
        return self

    def __next__(self):
        if not self.gpu >= 0:
            return next(self.iterator_)

        if not self.prefetch:
            return _to_device(next(self.iterator_), self.device, non_blocking=True)

        torch.cuda.current_stream().wait_stream(self.stream)

        batch = self._next
        if batch is None:
            raise StopIteration

        self.preload()

        return batch


@dataclass(frozen=True)
class Parameters(Serializable):
    modelname: str
    modelparams: Dict[str, Any]
    batch_size: int
    epochs: int

    loss: Loss
    optimizer: Union[Optimizer, Dict[str, Optimizer]]
    metrics: List[Metric] = field(default_factory=list)

    random_state: Optional[int] = None
    lr_scheduler: Optional[Union[LRScheduler, Dict[str, LRScheduler]]] = None

    sampler: Optional[Sampler] = None


InputShape = Union[
    Tuple[int, ...],
    Tuple[Tuple[int, ...], ...],
    List[Tuple[int, ...]],
    Dict[str, Tuple[int, ...]],
]


class Estimator:
    Params = Parameters

    def __init__(
        self,
        params: Parameters,
        input_shape: InputShape,
        output_shape: Union[Tuple[int, ...], Tuple[Tuple[int, ...], ...]],
    ):
        self.params = params
        self.input_shape = input_shape
        self.output_shape = output_shape

        self.lossfunc = self.params.loss()

        self.history = History()

        self.compiled = False

    def __compile_if_required(self):
        if not self.compiled:
            self.model = dynamic_load(self.params.modelname)(
                input_shape=self.input_shape,
                output_shape=self.output_shape,
                **self.params.modelparams,
            )

            self.optim = OptimizerWrapper.from_model(self.model, self.params.optimizer)

            if self.params.lr_scheduler is not None:
                self.lr_scheduler = LRSchedulerWrapper.from_optimizer(
                    self.optim.optimizer, self.params.lr_scheduler
                )
            else:
                self.lr_scheduler = None

            self.compiled = True

    @property
    def complexity(self):
        if hasattr(self.model, "complexity"):
            return self.model.complexity
        raise NotImplementedError("complexity is not implemented in the model")

    def save(self, path: str):
        """Save estimator's current state to the path.
        """
        torch.save(
            {
                "model": self.model.state_dict(),
                "optim": self.optim.state_dict(),
                "lr_scheduler": self.lr_scheduler.state_dict()
                if self.lr_scheduler is not None
                else None,
                "history": self.history.history,
                "epoch": self.history.epoch,
                "params": self.params.serialize(),
                "input_shape": self.input_shape,
                "output_shape": self.output_shape,
            },
            path,
        )

    def load(self, path: str, model_weight_only: bool = False):
        """Load Estimator state to current model

        Args:
            path              : Path to the checkpoint file.
            model_weight_only : Only restores model's weight when uses
                                transfer learning or distirations.
        """
        dic = torch.load(path, map_location=lambda storage, loc: storage)
        self.__compile_if_required()
        self.model.load_state_dict(dic["model"])

        if model_weight_only:
            return

        self.optim.load_state_dict(dic["optim"])
        if self.lr_scheduler is not None:
            self.lr_scheduler.load_state_dict(dic["lr_scheduler"])
        self.history.history = dic["history"]
        self.history.epoch = dic["epoch"]

    @classmethod
    def restore(cls, path: str) -> "Estimator":
        """Restore Estimator instance from stored snapshot.
        """
        dic = torch.load(path, map_location=lambda storage, loc: storage)
        m = cls(
            params=deserialize(dic["params"]),
            input_shape=dic["input_shape"],
            output_shape=dic["output_shape"],
        )
        m.load(path)
        return m

    def _prob_transform(self, logits) -> torch.Tensor:
        """Transform logits to probabilities.
        """
        if hasattr(self.model, "prob_transform"):
            return self.model.prob_transform(logits)
        return nn.functional.softmax(logits, dim=-1)

    def predict(
        self,
        X,
        batch_size: int = 32,
        gpu: int = -1,
        num_workers: int = 0,
        apply_func: Optional[Callable] = None,
        random_state: Optional[int] = None,
        **kwargs,
    ):
        return self.apply(
            "forward",
            X,
            batch_size=batch_size,
            gpu=gpu,
            num_workers=num_workers,
            apply_func=apply_func,
            random_state=random_state,
            **kwargs,
        )

    def predict_proba(
        self,
        X,
        batch_size: int = 32,
        gpu: int = -1,
        num_workers: int = 0,
        apply_func: Optional[Callable] = None,
        random_state: int = None,
        **kwargs,
    ):
        return self.apply(
            "forward",
            X,
            batch_size=batch_size,
            gpu=gpu,
            num_workers=num_workers,
            apply_func=apply_func,
            transform=self._prob_transform,
            random_state=random_state,
            **kwargs,
        )

    def apply(
        self,
        func: Union[str, Callable],
        X,
        batch_size: int = 32,
        gpu: int = -1,
        num_workers: int = 0,
        apply_func: Optional[Callable] = None,
        transform: Optional[Callable] = None,
        random_state: Optional[int] = None,
        drop_last: bool = False,
        **kwargs,
    ):
        """
        Args:
            func: Function to be used to execute with given data. If string, then try to find the function
                  in model's method. If function given, then it will be directly used.
        """
        device = _gpu_id_to_device(gpu)

        if random_state is not None:
            set_seed(random_state)

        self.model.to(device)
        self.model.eval()

        if apply_func is not None:
            self.model.apply(apply_func)

        dataset = _to_dataset(X)

        loader = DataLoader(
            dataset,
            batch_size=batch_size,
            shuffle=False,
            num_workers=num_workers,
            pin_memory=gpu >= 0,
            drop_last=drop_last,
        )

        if isinstance(func, str):
            model_func = getattr(self.model, func)
        else:
            model_func = func

        with torch.no_grad():

            preds = _PredictionQueue()

            for x in data_prefetcher(loader, device, gpu, prefetch=True):

                out = model_func(x, **kwargs)

                if transform is not None:
                    out = transform(out)

                preds.push(out)

            return preds.concat()

    def fit(  # noqa
        self,
        X,
        y=None,
        val_data: Optional[Tuple] = None,
        gpu: int = -1,
        num_workers: int = 0,
        verbose: int = 0,
        callbacks: Optional[List[Callback]] = None,
        prefetch: bool = True,
        drop_last: bool = False,
    ):
        """
        Args:
            X         : Input data to the estimator. Accepts np.ndarray, torch.tensor, Dataset,
                        and its list, tuple or dict.
            y         : Label data to the estimator. Accepts np.ndarray, torch.tensor, Dataset,
                        and its list, tuple or dict.
            val_data  : Tuple of X and y, expect to have same shape with original X and y.
            gpu       : -1 is for GPU, else indicates id to the gpu. Now only 1 GPU training is
                        supported.
            callbacks : List of callbacks which triggers every step of training.
            prefetch  : Whether to support prefetch of batch or not. If true, asyncrously send
                        batch to gpu to reduce the I/O waits.
        """
        batch_size = self.params.batch_size

        epochs = self.params.epochs

        # Enable cudnn algorithm optimization, most of case it is useful and
        # should make it faster to train the model. Except when input shape is
        # changing as it trained.
        if gpu >= 0:
            torch.backends.cudnn.benchmark = True  # type: ignore

        rnd = self.params.random_state
        if rnd is not None:
            set_seed(rnd)

        # After fix the seed with given randomstate, we'll initialize model, as those
        # weight init functions are dependent.
        self.__compile_if_required()

        device = _gpu_id_to_device(gpu)

        self.model.to(device)

        self.lossfunc.to(device)

        has_val_data = val_data is not None

        train_dataset = _to_dataset(X, y)

        sampler = self.params.sampler.build(self, X, y) if self.params.sampler else None

        train_loader = DataLoader(
            train_dataset,
            batch_size=batch_size,
            shuffle=self.params.sampler is None,
            num_workers=num_workers,
            pin_memory=gpu >= 0,
            sampler=sampler,  # type: ignore
            drop_last=drop_last,
        )

        if has_val_data:
            assert val_data is not None
            val_dataset = _to_dataset(*val_data)
            val_loader = DataLoader(
                val_dataset,
                batch_size=batch_size,
                shuffle=False,
                num_workers=num_workers,
                pin_memory=gpu >= 0,
                drop_last=drop_last,
            )

        samples = len(train_dataset)

        params = {
            "size": batch_size,
            "epochs": epochs,
            "verbose": verbose,
            "samples": samples,
            "metrics": _metrics_to_names(self.params.metrics, has_val_data),
        }

        callback = CallbackList([self.history] + (callbacks or []))  # type: ignore

        if self.lr_scheduler:
            for cb in self.lr_scheduler.to_callbacks():
                callback.append(cb)

        if verbose > 0:
            callback.append(ProgbarLogger())

        callback.set_model(self)
        callback.set_params(params)

        callback.on_train_begin(params)

        # initial_epoch will be different if restored from checkpoint.
        # At on_train_begin, it will restore the state from checkpoint and build history, so need to be after the
        # on_train_begin call
        initial_epoch = len(self.history.epoch)

        train_metrics = Metrics(self.params.metrics)
        val_metrics = Metrics(self.params.metrics)

        # Overwrites of default behaviors
        train_step = getattr(self.model, "train_step", default_train_step)
        val_step = getattr(self.model, "validation_step", default_validation_step)

        for epc in range(initial_epoch, epochs):
            logs = {"size": batch_size}
            callback.on_epoch_begin(epc, logs)

            self.model.train()
            train_metrics.reset()

            for batch_idx, batch in enumerate(
                data_prefetcher(train_loader, device, gpu, prefetch=prefetch)
            ):
                callback.on_batch_begin(batch_idx, logs)

                outputs = train_step(
                    batch=batch,
                    model=self.model,
                    criterion=self.lossfunc,
                    optimizer=self.optim,
                    batch_idx=batch_idx,
                )

                train_metrics.update(outputs)

                if verbose == 1 or verbose == True:
                    # This when syncronize the metrics, it is also calculate the
                    # metrics on the fly. And for the some of the metrics (one
                    # expect to use all samples to compute metrics), we do not
                    # want to calculate it every time as it is very slow.
                    # It is recommended to disable verbose mode on production env.
                    train_metrics.sync_to(logs)

                callback.on_batch_end(batch_idx, logs)

            train_metrics.sync_to(logs)

            if has_val_data:
                callback.on_validation_begin(logs)

                self.model.eval()
                val_metrics.reset()

                with torch.no_grad():

                    for batch_idx, batch in enumerate(
                        data_prefetcher(val_loader, device, gpu, prefetch=prefetch)
                    ):

                        outputs = val_step(
                            batch=batch,
                            model=self.model,
                            criterion=self.lossfunc,
                            batch_idx=batch_idx,
                        )

                        val_metrics.update(outputs)

                    val_metrics.sync_to(logs, prefix="val_")

                callback.on_validation_end(logs)

            callback.on_epoch_end(epc, logs)

        callback.on_train_end(params)

        return self


def default_validation_step(
    batch, model: nn.Module, criterion: Callable, batch_idx: int
) -> dict:
    """One validation step for a batch.

    Returns:
        Dict of tensors, which is used to calculate metrics.
    """
    x, y = batch

    logits: torch.Tensor = model(x)

    loss: torch.Tensor = criterion(logits, y["targets"])

    return {"loss": loss, "logits": logits, **y}


def default_train_step(
    batch, model: nn.Module, criterion: Callable, optimizer: Any, batch_idx: int
) -> dict:
    """One training step for a batch.

    Returns:
        Dict of tensors, which is used to calculate metrics.
    """
    x, y = batch

    optimizer.zero_grad()

    logits: torch.Tensor = model(x)

    loss: torch.Tensor = criterion(logits, y["targets"])

    loss.backward()

    optimizer.step()

    return {"loss": loss, "logits": logits, **y}


def _to_dataset(x, y=None):
    x = _to_tensor(x)

    has_y = y is not None

    if has_y:
        y = _to_tensor(y)

        if isinstance(y, dict):
            assert "targets" in y
        else:
            y = {"targets": y}

    if has_y:
        return XYDataset(x, y)
    return XDataset(x)


def _to_tensor(x):
    if isinstance(x, (list, tuple)):
        return x.__class__([_to_tensor(xi) for xi in x])

    if isinstance(x, dict):
        return {k: _to_tensor(v) for k, v in x.items()}

    if isinstance(x, (pd.Series, pd.DataFrame)):
        x = x.values

    if isinstance(x, np.ndarray):
        to_tensor = get_to_tensor(x[0])
        return to_tensor(x)
    return x


def get_to_tensor(x):
    """Convert one sample to dtype
    """

    if isinstance(x, np.ndarray):
        fn = torch.from_numpy
    else:
        fn = torch.tensor

    if x.dtype in (np.float32, np.float64, "f"):
        return lambda x: fn(x).float()
    elif x.dtype in (np.int32, np.int64, "i"):
        return lambda x: fn(x.tolist()).long()

    raise ValueError(f"{x} is uninterpletable dtype")


def _metrics_to_names(metrics, has_val_data):
    names = [m.name for m in metrics]
    if has_val_data:
        names = names + ["val_" + m.name for m in metrics]
    return names


def _gpu_id_to_device(gpu):
    if gpu >= 0:
        device = torch.device(gpu)
        torch.cuda.set_device(gpu)
    else:
        device = torch.device("cpu")
    return device


class _PredictionQueue:
    def __init__(self):
        self._q = None

    def push(self, batch):
        if isinstance(batch, (list, tuple)):
            q = self._q or batch.__class__([[] for _ in range(len(batch))])
            for i, item in enumerate(batch):
                q[i].append(item.cpu().numpy())
        elif isinstance(batch, dict):
            q = self._q or defaultdict(list)
            for k, item in batch.items():
                q[k].append(item.cpu().numpy())
        else:
            q = self._q or []
            q.append(batch.cpu().numpy())
        self._q = q

    def concat(self):
        if isinstance(self._q, (list, tuple)):
            if isinstance(self._q[0], list):
                return self._q.__class__([np.concatenate(v) for v in self._q])
            else:
                return np.concatenate(self._q)
        elif isinstance(self._q, dict):
            return {k: np.concatenate(v) for k, v in self._q.items()}
        raise NotImplementedError


class LRSchedulerWrapper:
    def __init__(self, lr_scheduler):
        self.lr_scheduler = lr_scheduler

    def to_callbacks(self):
        schedulers = []

        if isinstance(self.lr_scheduler, list):
            schedulers = self.lr_scheduler
        elif isinstance(self.lr_scheduler, dict):
            schedulers = [v for v in self.lr_scheduler.values()]
        else:
            schedulers = [self.lr_scheduler]

        return [
            LambdaCallback(lambda *args, **kwargs: s.step(), on=s.schedule_on)
            for s in schedulers
        ]

    def state_dict(self):
        if isinstance(self.lr_scheduler, list):
            return [s.state_dict() for s in self.lr_scheduler]
        if isinstance(self.lr_scheduler, dict):
            return {k: s for k, s in self.lr_scheduler}
        return self.lr_scheduler.state_dict()

    def load_state_dict(self, state):
        if isinstance(self.lr_scheduler, list):
            for a, b in zip(self.lr_scheduler, state):
                a.load_state_dict(b)
        if isinstance(self.lr_scheduler, dict):
            for k, v in self.lr_scheduler.items():
                v.load_state_dict(state[k])
        self.lr_scheduler.load_state_dict(state)

    @classmethod
    def from_optimizer(
        cls, optimizer: Any, lr_scheduler: Union[LRScheduler, Dict[str, LRScheduler]]
    ):

        if isinstance(lr_scheduler, LRScheduler):
            if isinstance(optimizer, list):
                return cls(lr_scheduler=[lr_scheduler(o) for o in optimizer])
            else:
                return cls(lr_scheduler=lr_scheduler(optimizer))
        if isinstance(lr_scheduler, dict):
            assert isinstance(optimizer, dict)
            return {key: lr_scheduler[key](o) for key, o in optimizer.items()}

        raise NotImplementedError


class OptimizerWrapper:
    def __init__(self, optimizer: Any):
        self.optimizer = optimizer

    @classmethod
    def from_model(self, model, optimizer: Union[Optimizer, Dict[str, Optimizer]]):
        if isinstance(optimizer, dict):
            return OptimizerWrapper(
                {k: v(getattr(model, k).parameters()) for k, v in optimizer.items()}
            )
        return OptimizerWrapper(optimizer(model.parameters()))

    def state_dict(self):
        if isinstance(self.optimizer, dict):
            return {k: v.state_dict() for k, v in self.optimizer.items()}
        return self.optimizer.state_dict()

    def load_state_dict(self, state):
        if isinstance(self.optimizer, dict):
            for k, v in self.optimizer.items():
                v.load_state_dict(state[k])
            return
        return self.optimizer.load_state_dict(state)

    def zero_grad(self):
        if isinstance(self, dict):
            for o in self.optimizer.values():
                o.zero_grad()
        else:
            self.optimizer.zero_grad()

    def step(self, closure=None):
        if isinstance(self, dict):
            for o in self.optimizer.values():
                o.step(closure)
        else:
            self.optimizer.step(closure)
