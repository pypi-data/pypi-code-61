# -*- coding: utf-8 -*-
from __future__ import print_function, division

import torch
import torch.nn as nn
import numpy as np
from pymic.layer.activation import get_acti_func
from pymic.layer.convolution import ConvolutionLayer
from pymic.layer.deconvolution import DeconvolutionLayer
from pymic.net2d.unet2d48 import UNetDenseBlock

class AttentionGateBlock(nn.Module):
    def __init__(self, chns_l, chns_h):
        super(AttentionGateBlock, self).__init__()
        self.in_chns_l = chns_l # channel number of low level features
        self.in_chns_h = chns_h # channel number of high level features

        self.out_chns = int(min(self.in_chns_l, self.in_chns_h)/2)
        self.conv1_l = nn.Conv2d(self.in_chns_l, self.out_chns,
                kernel_size = 1, bias = True)
        self.conv1_h = nn.Conv2d(self.in_chns_h, self.out_chns,
                kernel_size = 1, bias = True)
        self.conv2 = nn.Conv2d(self.out_chns, 1,
                kernel_size = 1, bias = True)
        self.act1 = nn.ReLU()
        self.act2 = nn.Sigmoid()

    def forward(self, x_l, x_h):
        input_shape = list(x_l.shape)
        gate_shape  = list(x_h.shape)

        # resize low-level feature to the shape of high-level feature
        x_l_reshape = nn.functional.interpolate(x_l, size = gate_shape[2:], mode = 'bilinear')
        f_l = self.conv1_l(x_l_reshape)
        f_h = self.conv1_h(x_h)
        f = f_l + f_h
        f = self.act1(f)
        f = self.conv2(f)
        att = self.act2(f)
        # resize attention map to the shape of low-level feature
        att = nn.functional.interpolate(att, size = input_shape[2:], mode = 'bilinear')
        output = att * x_l
        return output

class UNet2D48AG(nn.Module):
    def __init__(self, params):
        super(UNet2D48AG, self).__init__()
        self.params = params
        self.in_chns   = self.params['in_chns']
        self.ft_chns   = self.params['feature_chns']
        self.n_class   = self.params['class_num']
        self.acti_func = self.params['acti_func']
        self.dropout   = self.params['dropout']
        assert(len(self.ft_chns) == 3)

        self.block1 = UNetDenseBlock(self.in_chns, self.ft_chns[0], 
            2, 'down', self.acti_func, self.params)

        self.block2 = UNetDenseBlock(self.ft_chns[0], self.ft_chns[1], 
            2, 'down', self.acti_func, self.params)

        self.block3 = UNetDenseBlock(self.ft_chns[1], self.ft_chns[2], 
            2, 'up', self.acti_func, self.params)

        self.block4 = UNetDenseBlock(self.ft_chns[1] + self.ft_chns[2], self.ft_chns[1], 
            2, 'up', self.acti_func, self.params)

        self.block5 = UNetDenseBlock(self.ft_chns[0] + self.ft_chns[1], self.ft_chns[0], 
            2, None, self.acti_func, self.params)

        self.conv = nn.Conv2d(self.ft_chns[0], self.n_class, 
            kernel_size = 3, padding = 1)

        self.block2att = AttentionGateBlock(self.ft_chns[1], self.ft_chns[2])
        self.block1att = AttentionGateBlock(self.ft_chns[0], self.ft_chns[1])
        if(self.dropout):
            self.drop1 = nn.Dropout(p=0.1)
            self.drop2 = nn.Dropout(p=0.2)
            self.drop3 = nn.Dropout(p=0.3)

    def forward(self, x):
        x_shape = list(x.shape)
        if(len(x_shape) == 5):
            [N, C, D, H, W] = x_shape
            new_shape = [N*D, C, H, W]
            x = torch.transpose(x, 1, 2)
            x = torch.reshape(x, new_shape)

        f1, d1 = self.block1(x)
        if(self.dropout):
            f1 = self.drop1(f1)
            d1 = self.drop1(d1)
        f2, d2 = self.block2(d1)
        if(self.dropout):
            f2 = self.drop2(f2)
            d2 = self.drop2(d2)
        f3, f3up = self.block3(d2)
        if(self.dropout):
            f3up = self.drop3(f3up)

        f2att = self.block2att(f2, f3)
        f2cat = torch.cat((f2att, f3up), dim = 1)
        f4, f4up = self.block4(f2cat)

        f1att = self.block1att(f1, f4)
        f1cat = torch.cat((f1att, f4up), dim = 1)        
        f5, _ = self.block5(f1cat)

        output = self.conv(f5)
        if(len(x_shape) == 5):
            new_shape = [N, D] + list(output.shape)[1:]
            output = torch.reshape(output, new_shape)
            output = torch.transpose(output, 1, 2)

        return output


if __name__ == "__main__":
    params = {'in_chns':4,
              'feature_chns':[16, 32, 48],
              'class_num': 2,
              'acti_func': 'relu',
              'dropout': True}
    Net = UNet2D48AG(params)
    Net = Net.double()

    x  = np.random.rand(4, 4, 5, 48, 48)
    xt = torch.from_numpy(x)
    xt = torch.tensor(xt)
    
    y = Net(xt)
    print(len(y.size()))
    y = y.detach().numpy()
    print(y.shape)
