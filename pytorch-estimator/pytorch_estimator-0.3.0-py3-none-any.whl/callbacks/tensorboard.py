import torch

from .base import Callback, Priority


class TensorBoard(Callback):
    def __init__(
        self, log_dir, add_graph=True, add_histogram=True, hist_freq=1, input_shape=None
    ):
        if add_graph:
            assert input_shape is not None
        from torch.utils.tensorboard import SummaryWriter

        self.writer = SummaryWriter(log_dir)
        self.input_shape = input_shape
        self.add_graph = add_graph
        self.add_histogram = add_histogram
        self.hist_freq = hist_freq

    @property
    def priority_order(self):
        return Priority.AFTER_HISTORY_RECORD

    def on_train_begin(self, logs=None):

        if self.add_graph:
            input_shape = self.input_shape
            d = next(self.model.model.parameters()).device
            if type(input_shape[0]) == int:
                v = torch.zeros(list([1] + list(input_shape))).to(d)
            else:
                v = tuple(
                    [
                        torch.zeros(list([1] + list(shape))).to(d)
                        for shape in input_shape
                    ]
                )
            self.writer.add_graph(self.model.model, v, verbose=False)

    def on_epoch_end(self, epoch, logs=None):
        if logs is not None:
            for k, v in logs.items():
                self.writer.add_scalar(k, v, global_step=epoch)

        if self.add_histogram and epoch % self.hist_freq == 0:
            for name, param in self.model.model.named_parameters():
                param = param.clone()
                self.writer.add_histogram(
                    name, param.cpu().data.numpy(), global_step=epoch
                )
                if param.grad is not None:
                    self.writer.add_histogram(
                        name, param.grad.cpu().data.numpy(), global_step=epoch
                    )
