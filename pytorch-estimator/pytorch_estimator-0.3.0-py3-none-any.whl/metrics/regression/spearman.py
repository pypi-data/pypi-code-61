from dataclasses import dataclass
from ..metric import EpochMetirc, MappingTransform, OutputTransform


def spearman_fn(y_preds, y_targets):
    try:
        from scipy.stats import spearmanr
    except ImportError:
        raise RuntimeError("This contrib module requires sklearn to be installed.")

    y_true = y_targets.numpy()
    y_pred = y_preds.numpy()

    r, _ = spearmanr(y_true, y_pred)

    return r


@dataclass(frozen=True)
class Spearman(EpochMetirc):
    name = "spearman"
    output_transform: OutputTransform = MappingTransform(
        input_names=["logits", "targets"]
    )

    def compute_fn(self, logits, targets):
        return spearman_fn(logits, targets)
