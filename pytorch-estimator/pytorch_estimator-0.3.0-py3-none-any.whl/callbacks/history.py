from datetime import datetime

from .base import Callback, Priority


class History(Callback):
    """Callback that records events into a `History` object.
    This callback is automatically applied to
    every Keras model. The `History` object
    gets returned by the `fit` method of models.
    """

    def __init__(self, *args, **kwargs):
        self.epoch = []
        self.history = {}

    @property
    def priority_order(self):
        return Priority.HISTORY_RECORD

    def on_epoch_begin(self, epoch, logs=None):
        self.start_ = datetime.now()

    def on_epoch_end(self, epoch, logs=None):
        logs = logs or {}
        self.epoch.append(epoch)
        for k, v in logs.items():
            self.history.setdefault(k, []).append(v)

        duration = round((datetime.now() - self.start_).total_seconds(), 2)
        self.history.setdefault("duration", []).append(duration)
