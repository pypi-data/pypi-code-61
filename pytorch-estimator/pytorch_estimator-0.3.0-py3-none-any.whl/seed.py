def set_seed(seed=43):
    import numpy as np
    import random as rn
    import torch

    np.random.seed(seed)

    rn.seed(seed)

    torch.manual_seed(seed)

    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)
