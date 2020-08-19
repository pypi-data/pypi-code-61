# -*- coding: utf-8 -*-
from __future__ import print_function, division

import torch
import torch.nn as nn
import numpy as np
from pymic.layer.activation import get_acti_func
from pymic.layer.convolution import ConvolutionLayer
from pymic.layer.deconvolution import DeconvolutionLayer
from pymic.net2d.unet2d48 import UNetDenseBlock
from pymic.net2d.unet2d48_ag import AttentionGateBlock

class UNet2D48D3AG(nn.Module):
    def __init__(self, params):
        super(UNet2D48D3AG, self).__init__()
        self.params = params
        self.in_chns   = self.params['in_chns']
        self.ft_chns   = self.params['feature_chns']
        self.n_class   = self.params['class_num']
        self.acti_func = self.params['acti_func']
        self.dropout   = self.params['dropout']
        assert(len(self.ft_chns) == 4)

        self.block1 = UNetDenseBlock(self.in_chns, self.ft_chns[0], 
            2, 'down', self.acti_func, self.params)

        self.block2 = UNetDenseBlock(self.ft_chns[0], self.ft_chns[1], 
            2, 'down', self.acti_func, self.params)

        self.block3 = UNetDenseBlock(self.ft_chns[1], self.ft_chns[2], 
            2, 'down', self.acti_func, self.params)

        self.block4 = UNetDenseBlock(self.ft_chns[2], self.ft_chns[3], 
            2, 'up', self.acti_func, self.params)

        self.block5 = UNetDenseBlock(self.ft_chns[2] + self.ft_chns[3], self.ft_chns[2], 
            2, 'up', self.acti_func, self.params)

        self.block6 = UNetDenseBlock(self.ft_chns[1] + self.ft_chns[2], self.ft_chns[1], 
            2, 'up', self.acti_func, self.params)

        self.block7 = UNetDenseBlock(self.ft_chns[0] + self.ft_chns[1], self.ft_chns[0], 
            2, None, self.acti_func, self.params)

        self.conv = nn.Conv2d(self.ft_chns[0], self.n_class, 
            kernel_size = 3, padding = 1)

        self.block3att = AttentionGateBlock(self.ft_chns[2], self.ft_chns[3])
        self.block2att = AttentionGateBlock(self.ft_chns[1], self.ft_chns[2])
        self.block1att = AttentionGateBlock(self.ft_chns[0], self.ft_chns[1])
        if(self.dropout):
            self.drop3 = nn.Dropout(p=0.2)
            self.drop4 = nn.Dropout(p=0.3)

    def forward(self, x):
        x_shape = list(x.shape)
        if(len(x_shape) == 5):
            [N, C, D, H, W] = x_shape
            new_shape = [N*D, C, H, W]
            x = torch.transpose(x, 1, 2)
            x = torch.reshape(x, new_shape)

        f1, d1 = self.block1(x)
        f2, d2 = self.block2(d1)
        f3, d3 = self.block3(d2)
        if(self.dropout):
            f3 = self.drop3(f3)
            d3 = self.drop3(d3)
        f4, f4up = self.block4(d3)
        if(self.dropout):
            f4 = self.drop4(f4)
            f4up = self.drop4(f4up)

        f3att = self.block3att(f3, f4)
        f3cat = torch.cat((f3att, f4up), dim = 1)
        f5, f5up = self.block5(f3cat)

        f2att = self.block2att(f2, f5)
        f2cat = torch.cat((f2att, f5up), dim = 1)        
        f6, f6up = self.block6(f2cat)

        f1att = self.block1att(f1, f6)
        f1cat = torch.cat((f1att, f6up), dim = 1)        
        f7, _ = self.block7(f1cat)

        output = self.conv(f7)
        if(len(x_shape) == 5):
            new_shape = [N, D] + list(output.shape)[1:]
            output = torch.reshape(output, new_shape)
            output = torch.transpose(output, 1, 2)

        return output


if __name__ == "__main__":
    params = {'in_chns':4,
              'feature_chns':[16, 32, 48, 64],
              'class_num': 2,
              'acti_func': 'relu',
              'dropout': True}
    Net = UNet2D48D3AG(params)
    Net = Net.double()

    x  = np.random.rand(4, 4, 5, 48, 48)
    xt = torch.from_numpy(x)
    xt = torch.tensor(xt)
    
    y = Net(xt)
    print(len(y.size()))
    y = y.detach().numpy()
    print(y.shape)
