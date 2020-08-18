import torch

from ..models.simple_mlp import MLP


class TupleMLP(MLP):
    def __init__(self, input_shape, **kwargs):
        super().__init__(input_shape=input_shape[0], **kwargs)

    def forward(self, x):
        assert isinstance(x, (tuple, list))
        return super().forward(x[0])


class DictMLP(MLP):
    def __init__(self, input_shape, **kwargs):
        super().__init__(input_shape=input_shape["dense_vector"], **kwargs)

    def forward(self, x):
        assert isinstance(x, dict)
        return super().forward(x["dense_vector"])


class TupleOutputMLP(MLP):
    def forward(self, x):
        return (super().forward(x), x)

    def prob_transform(self, x):
        return torch.softmax(x[0], dim=-1)

    @staticmethod
    def validation_step(batch, model, criterion, batch_idx):
        x, y = batch

        logits = model(x)

        loss = criterion(logits[0], y["targets"])

        return {"loss": loss, "logits": logits[0], **y}

    @staticmethod
    def train_step(batch, model, criterion, optimizer, batch_idx):
        x, y = batch

        logits = model(x)

        loss = criterion(logits[0], y["targets"])

        loss.backward()

        optimizer.step()

        return {"loss": loss, "logits": logits[0], **y}


class DictOutputMLP(MLP):
    def forward(self, x):
        return {"logits": super().forward(x), "x": x}

    def prob_transform(self, x):
        return torch.softmax(x["logits"], dim=-1)

    @staticmethod
    def validation_step(batch, model, criterion, batch_idx):
        x, y = batch

        logits = model(x)

        loss = criterion(logits["logits"], y["targets"])

        return {"loss": loss, "logits": logits["logits"], **y}

    @staticmethod
    def train_step(batch, model, criterion, optimizer, batch_idx):
        x, y = batch

        logits = model(x)

        loss = criterion(logits["logits"], y["targets"])

        loss.backward()

        optimizer.step()

        return {"loss": loss, "logits": logits["logits"], **y}
