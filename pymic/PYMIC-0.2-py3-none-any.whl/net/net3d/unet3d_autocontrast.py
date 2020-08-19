# -*- coding: utf-8 -*-
from __future__ import print_function, division

import torch
import torch.nn as nn
import numpy as np
from pymic.net3d.unet3d import UNet3D

def get_base_network(params):
    net_type = params['net_type']
    if(net_type == 'UNet3D'):
        return UNet3D(params)
    else:
        raise ValueError("undefined network {0:}".format(net_type))

class AutoContrastLayer(nn.Module):
    def __init__(self, init_level, init_window, trans_func):
        super(AutoContrastLayer, self).__init__()
        
        self.level = torch.nn.Parameter(torch.tensor(init_level))
        self.logw  = torch.nn.Parameter(torch.log(torch.tensor(init_window)))
        self.level.requires_grad = True 
        self.logw.requires_grad  = True
        self.trans_func = trans_func
        # self.level = torch.tensor(init_level)
        # self.logw  = torch.tensor(math.log(init_window))    

    def forward(self, x):
        window = torch.exp(self.logw)
        x0 = self.level - window / 2
        x1 = self.level + window / 2
        if(self.trans_func == 'sigmoid'):
            sig0 = torch.sigmoid(x - x0)
            sig1 = torch.sigmoid(x - x1)
            y = (x - x0) * (sig0 - sig1) / window + sig1 
        else:
            mask1 = x < x0 
            mask2 = (x >= x0) * (x <= x1)
            mask3 = x > x1
            x_min = -3100.0
            x_max = 2000.0
            # for segment 1
            y1 = mask1 * ((x - x_min) / (x0 - x_min) * 0.1)
            y2 = mask2 * ((x - x0) / (x1 - x0) * 0.8 + 0.1)
            y3 = mask3 * ((x - x1) / (x_max - x1) * 0.1 + 0.9)
            y = y1 + y2 + y3
        return y

class UNet3DAutoContrast(nn.Module):
    def __init__(self, params):
        super(UNet3DAutoContrast, self).__init__()
        init_level  = params['init_level']
        init_window = params['init_window']
        trans_func  = params['trans_func']
        self.contrast_layer = AutoContrastLayer(init_level, init_window, trans_func)
        params['net_type'] = params['base_net_type']
        self.net =  get_base_network(params)

    def forward(self, x):
        output = self.contrast_layer(x)
        output = self.net(output)
        return output

if __name__ == "__main__":
    params = {'base_net_type': 'UNet3D',
              'init_level': -150.0,
              'init_window': 700.0,
              'in_chns':4,
              'feature_chns':[2, 8, 32, 48, 64],
              'class_num': 2, 
              'acti_func': 'LeakyReLU',
              'leakyrelu_negative_slope': 0.01,
              'dropout': 0.3}
    Net = UNet3DAutoContrast(params)
    Net = Net.double()

    x  = np.random.rand(4, 4, 96, 96, 96)
    xt = torch.from_numpy(x)
    xt = torch.tensor(xt)
    
    y = Net(xt)
    y = y.detach().numpy()
    print(y.shape)
    print(y)
