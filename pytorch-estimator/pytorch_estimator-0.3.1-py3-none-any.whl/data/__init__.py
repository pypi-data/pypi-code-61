from torch.utils.data import Dataset


class XYDataset(Dataset):
    """Dataset for torch.utils.DataLoader.

    This class is used when X is a tuple or list.
    """

    def __init__(self, x, y):
        self.datasets = [x, y]
        self._fn_x = _generate_getitem(x)
        self._fn_y = _generate_getitem(y)
        self._n = _length(x)

    def __getitem__(self, index):
        X, y = self.datasets
        return (self._fn_x(X, index), self._fn_y(y, index))

    def __len__(self):
        return self._n


class XDataset(Dataset):
    def __init__(self, x):
        self.datasets = x
        self._fn_x = _generate_getitem(x)
        self._n = _length(x)

    def __getitem__(self, index):
        return self._fn_x(self.datasets, index)

    def __len__(self):
        return self._n


def _generate_getitem(x):
    if isinstance(x, (list, tuple)):
        return lambda y, index: tuple(yi[index] for yi in y)
    if isinstance(x, dict):
        return lambda y, index: {key: yi[index] for key, yi in y.items()}
    return lambda y, index: y[index]


def _length(x):
    if isinstance(x, (list, tuple)):
        return len(x[0])
    if isinstance(x, dict):
        return len(list(x.values())[0])
    return len(x)
