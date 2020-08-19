import torch 
import time 
import numpy as np 

from pymic.net3d.unetnd_extention import UNetND_Extention

def test_2d_networks():
    methods = ["UNetBlock", 
               "UNetBlock_DW", 
               "UNetBlock_DW", # GC
               "UNetBlock_DW_CF", # GC
               "UNetBlock_DW_CF", # GC, DSP
               "UNetBlock_DW_CF_Res"] #GC, DSP
    method_id = 5
    if(method_id > 1):
        feature_grps = [1, 2,  2,  4,  4]
    else:
        feature_grps = [1, 1, 1, 1, 1]
    deep_sup = True if method_id > 3 else False
    
    params = {'dimension': 2, 
              'in_chns': 1,
              'feature_chns':[16, 32, 64, 128, 256],
              'feature_grps':feature_grps,
              'class_num'   : 2,
              'block_type'  : methods[method_id],
              'norm_type'   : 'batch_norm',
              'acti_func': 'relu',
              'dropout'  : True,
              'depth_sep_deconv' : True, 
              'deep_supervision': deep_sup}
    print('block type', methods[method_id])
    Net = UNetND_Extention(params)
    Net = Net.double()
    device = torch.device('cuda:1')
    Net.to(device)
    x  = np.random.rand(1, 1, 96, 96, 96) # N, C, H, W
    xt = torch.from_numpy(x)
    xt = torch.tensor(xt)
    xt = xt.to(device)
    t_list = []
    for i in range(10):
        t0 = time.time()
        y  = Net(xt)
        t  = time.time()  - t0 
        t_list.append(t)
    t_array = np.asarray(t_list)
    print('time', t_array.mean())
    if(isinstance(y, tuple)):
        y  = y[0]
    print(len(y.size()))
    y = y.detach().cpu().numpy()
    print(y.shape)

def test_3d_networks():
    methods = ["UNetBlock", 
               "UNetBlock_DW",
               "UNetBlock_SpatialSep", 
               "UNetBlock_SpatialDepthSep"]
    method_id = 3
    if(method_id > 3):
        feature_grps = [1, 2,  2,  4,  4]
    else:
        feature_grps = [1, 1, 1, 1, 1]
    deep_sup = True if method_id > 3 else False
    
    params = {'dimension': 3, 
              'in_chns': 1,
              'feature_chns':[32, 64, 128, 256],
              'feature_grps':feature_grps,
              'class_num'   : 2,
              'block_type'  : methods[method_id],
              'norm_type'   : 'batch_norm',
              'acti_func': 'relu',
              'dropout'  : True,
              'depth_sep_deconv' : True, 
              'deep_supervision': deep_sup}
    print('block type', methods[method_id])
    Net = UNetND_Extention(params)
    Net = Net.float()
    device = torch.device('cuda:0')
    Net.to(device)
    x  = np.random.rand(4, 1, 48, 48, 48) # N, C, H, W
    xt = torch.from_numpy(x)
    xt = torch.tensor(xt).float()
    xt = xt.to(device)
    t_list = []
    for i in range(10):
        t0 = time.time()
        y  = Net(xt)
        t  = time.time()  - t0 
        t_list.append(t)
    t_array = np.asarray(t_list)
    print('time', t_array.mean())
    if(isinstance(y, tuple)):
        y  = y[0]
    print(len(y.size()))
    y = y.detach().cpu().numpy()
    print(y.shape)

if __name__ == "__main__":
    test_3d_networks()