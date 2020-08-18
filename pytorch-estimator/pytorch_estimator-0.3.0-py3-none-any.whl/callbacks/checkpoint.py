import os
import glob
from pathlib import Path
import re

from .base import Callback, Priority


class Checkpoint(Callback):
    def __init__(self, path: str, autorestore: bool = True):
        self.path = path
        self.autorestore = autorestore

    @property
    def priority_order(self):
        return Priority.AFTER_HISTORY_RECORD

    def on_train_begin(self, logs=None):
        if not self.autorestore:
            return

        epochs = []

        files = glob.glob(str(Path(self.path)) + "/*.pth")

        for s in files:
            m = re.match(".*/([0-9]+).pth", s)
            if m:
                epochs.append(int(m[1]))

        if len(epochs) == 0:
            return

        epc = max(epochs)

        self.model.load(str(Path(self.path).joinpath(f"{epc}.pth")))

        print(f"Restore epoch = {epc}")

    def on_epoch_end(self, epoch, logs=None):
        ckpt_path = Path(self.path).joinpath(f"{epoch}.pth")

        ckpt_dir = os.path.dirname(ckpt_path)

        os.makedirs(ckpt_dir, exist_ok=True)

        self.model.save(ckpt_path)
