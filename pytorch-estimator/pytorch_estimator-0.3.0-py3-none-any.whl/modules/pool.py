import torch.nn as nn


class flatten(nn.Module):
    def forward(self, x):
        return x.view(x.size(0), -1)


class global_avg_pool(nn.Module):
    def __init__(self, **kwargs):
        super().__init__()
        self.avg_pool = nn.AdaptiveAvgPool1d(1)

    def forward(self, x):
        return self.avg_pool(x).view(x.size(0), -1)
