import torch
import os
import platform

if platform.system().lower() == 'darwin':
    torch.ops.load_library(os.path.join(os.path.dirname(__file__), 'liblanms.dylib'))
elif platform.system().lower() == 'linux':
    torch.ops.load_library(os.path.join(os.path.dirname(__file__), 'liblanms.so'))


def merge_quadrangle_n9(polys, thres=0.3, precision=10000):
    if len(polys) == 0:
        return torch.tensor([], dtype=torch.double)
    p = polys.clone()
    p[:, :8] *= precision
    ret = torch.ops.lanms.merge_quadrangle_n9(p, thres)
    ret[:, :8] /= precision
    return ret

