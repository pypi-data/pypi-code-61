import enum


class Priority(enum.IntEnum):
    DEFAULT = 100
    HISTORY_RECORD = 200
    AFTER_HISTORY_RECORD = 300


class CallbackList:
    """Container abstracting a list of callbacks.
    # Arguments
        callbacks: List of `Callback` instances.
        queue_length: Queue length for keeping
            running statistics over callback execution time.
    """

    def __init__(self, callbacks=None):
        callbacks = callbacks or []
        self.callbacks = [c for c in callbacks]
        self.callbacks.sort()

    def append(self, callback):
        self.callbacks.append(callback)
        self.callbacks.sort()

    def set_params(self, params):
        for callback in self.callbacks:
            callback.set_params(params)

    def set_model(self, model):
        for callback in self.callbacks:
            callback.set_model(model)

    def on_epoch_begin(self, epoch, logs=None):
        """Called at the start of an epoch.
        # Arguments
            epoch: integer, index of epoch.
            logs: dictionary of logs.
        """
        logs = logs or {}
        for callback in self.callbacks:
            callback.on_epoch_begin(epoch, logs)

    def on_epoch_end(self, epoch, logs=None):
        """Called at the end of an epoch.
        # Arguments
            epoch: integer, index of epoch.
            logs: dictionary of logs.
        """
        logs = logs or {}
        for callback in self.callbacks:
            callback.on_epoch_end(epoch, logs)

    def on_batch_begin(self, batch, logs=None):
        """Called right before processing a batch.
        # Arguments
            batch: integer, index of batch within the current epoch.
            logs: dictionary of logs.
        """
        logs = logs or {}
        for callback in self.callbacks:
            callback.on_batch_begin(batch, logs)

    def on_batch_end(self, batch, logs=None):
        """Called at the end of a batch.
        # Arguments
            batch: integer, index of batch within the current epoch.
            logs: dictionary of logs.
        """
        logs = logs or {}
        for callback in self.callbacks:
            callback.on_batch_end(batch, logs)

    def on_train_begin(self, logs=None):
        """Called at the beginning of training.
        # Arguments
            logs: dictionary of logs.
        """
        logs = logs or {}
        for callback in self.callbacks:
            callback.on_train_begin(logs)

    def on_train_end(self, logs=None):
        """Called at the end of training.
        # Arguments
            logs: dictionary of logs.
        """
        logs = logs or {}
        for callback in self.callbacks:
            callback.on_train_end(logs)

    def on_validation_begin(self, logs=None):
        """Called at the beginning of validation.
        # Arguments
            logs: dictionary of logs.
        """
        logs = logs or {}
        for callback in self.callbacks:
            callback.on_validation_begin(logs)

    def on_validation_end(self, logs=None):
        """Called at the end of validation.
        # Arguments
            logs: dictionary of logs.
        """
        logs = logs or {}
        for callback in self.callbacks:
            callback.on_validation_end(logs)

    def __iter__(self):
        return iter(self.callbacks)


class Callback(object):
    def __init__(self):
        self.model = None

    @property
    def priority_order(self):
        """Lower priority_order callbacks should appear earlier in the callbacks list.
        Has more dependent callbacks -> lower priority_order
        """
        return Priority.DEFAULT

    def set_params(self, params):
        self.params = params

    def set_model(self, model):
        self.model = model

    def on_epoch_begin(self, epoch, logs=None):
        pass

    def on_epoch_end(self, epoch, logs=None):
        pass

    def on_validation_begin(self, epoch, logs=None):
        pass

    def on_validation_end(self, epoch, logs=None):
        pass

    def on_batch_begin(self, batch, logs=None):
        pass

    def on_batch_end(self, batch, logs=None):
        pass

    def on_train_begin(self, logs=None):
        pass

    def on_train_end(self, logs=None):
        pass

    def __eq__(self, other):
        assert isinstance(other, Callback), "Cannot compare"
        return self.priority_order == other.priority_order

    def __lt__(self, other):
        assert isinstance(other, Callback), "Cannot compare"
        return self.priority_order < other.priority_order

    def __gt__(self, other):
        assert isinstance(other, Callback), "Cannot compare"
        return self.priority_order > other.priority_order


class LambdaCallback(Callback):
    def __init__(self, func, on="epoch_end"):
        self.func = func
        self.on = on
        assert on in ("epoch_end", "batch_end")

    def on_epoch_end(self, epoch, logs=None):
        if self.on == "epoch_end":
            self.func(epoch, logs=None)

    def on_batch_end(self, batch, logs=None):
        if self.on == "batch_end":
            self.func(batch, logs=None)
