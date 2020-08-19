import torch 
import time 
import numpy as np 
from pymic.net2d.unet2d import UNet2D
from pymic.net2d.unet2dres import UNet2DRes
from pymic.net3d.unetnd_extention import UNetND_Extention
from pymic.net2d.deeplabv3_plus import DeepLabv3plus
from pymic.net2d.eespnet_v2 import EESPNetV2

def get_network_parameter_number(net):
    param_number = sum(p.numel() for p in net.parameters() if p.requires_grad)
    return param_number

def test_network(net, tensor_type = 'float'):
    device = torch.device('cuda:1')
    net.to(device)
    xt = torch.randn(2, 1, 8, 128, 128)
    if(tensor_type == 'double'):
        net = net.double()
        xt = xt.double()
    xt = xt.to(device)
    t_list = []
    for i in range(10):
        t0 = time.time()
        y = net(xt)
        t  = time.time()  - t0 
        t_list.append(t)
    t_array = np.asarray(t_list)
    print('time', t_array.mean())
    print(len(y.size()))
    y = y.detach().cpu().numpy()
    print(y.shape)

    model_size = get_network_parameter_number(net)
    print('model size', model_size)

def test_unet2d():
    params = {'in_chns':1,
              'feature_chns':[32, 64, 128, 256, 512],
              'class_num': 2,
              'dropout': 0.2,
              'acti_func': 'relu'}
    Net = UNet2D(params)
    test_network(Net, 'float')
    test_network(Net, 'double')

def test_uent2d_2():
    params = {'class_num': 2,
              'in_chns':1,
              'block_type': 'UNetBlock',
              'feature_chns':[32, 64, 128, 256, 512],
              'feature_grps':[ 1,  1,   1,   1,   1],
              'norm_type':   'batch_norm',
              'acti_func': 'leakyrelu',
              'leakyrelu_negative_slope': 0.01,
              'dropout': 0.2,
              'depth_sep_deconv': False,
              'deep_supervision': False}
    Net = UNet2DRes(params)
    test_network(Net, 'float')
    test_network(Net, 'double')

def test_unetnd_extention():
    params = {'class_num': 2,
              'dimension': 2,
              'in_chns':1,
              'block_type': 'UNetBlock',
              'feature_chns':[32, 64, 128, 256, 512],
              'feature_grps':[ 1,  1,   1,   1,   1],
              'norm_type':   'batch_norm',
              'acti_func': 'leakyrelu',
              'leakyrelu_negative_slope': 0.01,
              'dropout': True,
              'depth_sep_deconv': False,
              'deep_supervision': False}
    Net = UNetND_Extention(params)
    test_network(Net, 'float')
    test_network(Net, 'double')

def test_deeplabv3plus():
    params = {'class_num': 2,
            'in_chns':1,
            'output_stride': 8}
    Net = DeepLabv3plus(params)
    test_network(Net, 'float')
    test_network(Net, 'double')

def test_espnetv2():
    params = {'class_num': 2,
        'in_chns':1,
        'output_stride': 1}
    Net = EESPNetV2(params)
    test_network(Net, 'float')
    test_network(Net, 'double')
if __name__ == "__main__":
    test_unet2d()
    # test_uent2d_2()
    # test_unetnd_extention()
    # test_deeplabv3plus()
    # test_espnetv2()