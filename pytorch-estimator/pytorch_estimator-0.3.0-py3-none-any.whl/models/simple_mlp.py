import math

import torch.nn as nn
import torch.nn.functional as F


class dense(nn.Module):
    def __init__(
        self, input_dim, output_dim, use_bias=True, dropout=0, activation="relu"
    ):
        super().__init__()
        self.dense = nn.Linear(input_dim, output_dim, bias=use_bias)
        self.act = getattr(F, activation, lambda x: x)
        if activation == "selu":
            self.dropout = nn.AlphaDropout(dropout)
        else:
            self.dropout = nn.Dropout(dropout)

    def forward(self, x):
        return self.dropout(self.act(self.dense(x)))


class MLP(nn.Module):
    def __init__(
        self,
        input_shape,
        output_shape,
        n_hidden_layers=1,
        hidden_layer_dim=32,
        use_bias=True,
        dropout=0,
        activation="relu",
        **kwargs
    ):
        super().__init__()
        if len(output_shape) == 0:
            n_classes = 1
            self.regression = True
        else:
            n_classes = output_shape[0]
            assert n_classes > 0
            self.regression = False

        self.input_dim = input_shape[0]
        self.n_hidden_layers = n_hidden_layers
        self.hidden_layer_dim = hidden_layer_dim
        self.output_dim = n_classes
        self.use_bias = use_bias
        self.dropout = dropout
        self.activation = activation
        self.n_layers = self.n_hidden_layers + 2

        layers = []
        for layer in range(self.n_layers):

            is_input_layer, is_output_layer = (layer == 0, layer > self.n_hidden_layers)

            input_dim = self.input_dim if is_input_layer else self.hidden_layer_dim

            output_dim = self.output_dim if is_output_layer else self.hidden_layer_dim

            activation = "identity" if is_output_layer else self.activation

            dropout = 0 if is_input_layer else self.dropout

            layers.append(
                dense(
                    input_dim=input_dim,
                    output_dim=output_dim,
                    use_bias=self.use_bias,
                    dropout=dropout,
                    activation=activation,
                )
            )

        self.seq = nn.Sequential(*layers)

    @property
    def complexity(self) -> float:
        # Approximation of the Rademacher complexity
        return math.sqrt(float(self.n_layers - 1))

    def forward(self, x):
        o = self.seq(x)

        if self.regression:
            o = o.reshape(-1)

        return o
