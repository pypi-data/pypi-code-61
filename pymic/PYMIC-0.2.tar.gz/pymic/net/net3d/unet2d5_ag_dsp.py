# -*- coding: utf-8 -*-
from __future__ import print_function, division

import torch
import torch.nn as nn
import numpy as np
from pymic.layer.activation import get_acti_func
from pymic.layer.convolution import ConvolutionLayer
from pymic.layer.deconvolution import DeconvolutionLayer
from pymic.net3d.unet2d5_ag import *

class UNet2D5AGDSP(nn.Module):
    def __init__(self, params):
        super(UNet2D5AGDSP, self).__init__()
        self.params = params
        self.in_chns   = self.params['in_chns']
        self.ft_chns   = self.params['feature_chns']
        self.n_class   = self.params['class_num']
        self.acti_func = self.params['acti_func']
        self.dropout   = self.params['dropout']
        assert(len(self.ft_chns) == 5)

        self.block1 = UNetBlock(self.in_chns, self.ft_chns[0], 
            2, 'down', self.acti_func, self.params)

        self.block2 = UNetBlock(self.ft_chns[0], self.ft_chns[1], 
            2, 'down', self.acti_func, self.params)

        self.block3 = UNetBlock(self.ft_chns[1], self.ft_chns[2], 
            2, 'down', self.acti_func, self.params)

        self.block4 = UNetBlock(self.ft_chns[2], self.ft_chns[3], 
            3, 'down', self.acti_func, self.params)

        self.block5 = UNetBlock(self.ft_chns[3], self.ft_chns[4], 
            3, 'up', self.acti_func, self.params)

        self.block6 = UNetBlock(self.ft_chns[3] + self.ft_chns[4] + self.n_class, self.ft_chns[3], 
            2, 'up', self.acti_func, self.params)

        self.block7 = UNetBlock(self.ft_chns[2] + self.ft_chns[3] + self.n_class, self.ft_chns[2], 
            2, 'up', self.acti_func, self.params)

        self.block8 = UNetBlock(self.ft_chns[1] + self.ft_chns[2] + self.n_class, self.ft_chns[1], 
            2, 'up', self.acti_func, self.params)

        self.block9 = UNetBlock(self.ft_chns[0] + self.ft_chns[1] + self.n_class, self.ft_chns[0], 
            2, None, self.acti_func, self.params)

        self.conv_b5 = nn.Conv3d(self.ft_chns[4], self.n_class, 
            kernel_size = (3, 3, 3), padding = (1, 1, 1))    

        self.conv_b6 = nn.Conv3d(self.ft_chns[3], self.n_class, 
            kernel_size = (1, 3, 3), padding = (0, 1, 1))   

        self.conv_b7 = nn.Conv3d(self.ft_chns[2], self.n_class, 
            kernel_size = (1, 3, 3), padding = (0, 1, 1))   

        self.conv_b8 = nn.Conv3d(self.ft_chns[1], self.n_class, 
            kernel_size = (1, 3, 3), padding = (0, 1, 1))   

        self.conv_b9 = nn.Conv3d(self.ft_chns[0], self.n_class, 
            kernel_size = (1, 3, 3), padding = (0, 1, 1))    

        self.block4att = AttentionGateBlock(self.ft_chns[3], self.ft_chns[4])
        self.block3att = AttentionGateBlock(self.ft_chns[2], self.ft_chns[3])
        self.block2att = AttentionGateBlock(self.ft_chns[1], self.ft_chns[2])
        self.block1att = AttentionGateBlock(self.ft_chns[0], self.ft_chns[1])

        if(self.dropout):
            self.drop4 = nn.Dropout(p=0.2)
            self.drop5 = nn.Dropout(p=0.3)

    def forward(self, x):
        f1, d1 = self.block1(x)
        f2, d2 = self.block2(d1)
        f3, d3 = self.block3(d2)
        f4, d4 = self.block4(d3)
        if(self.dropout):
            f4 = self.drop4(f4)
            d4 = self.drop4(d4)
        f5, f5up = self.block5(d4)
        if(self.dropout):
            f5 = self.drop5(f5)
            f5up = self.drop5(f5up)

        f5pred = self.conv_b5(f5)
        f5predup = nn.functional.interpolate(f5pred, 
                    size = list(f4.shape)[2:], mode = 'trilinear')
        f5predup_out = nn.functional.interpolate(f5pred, 
                    size = list(x.shape)[2:], mode = 'trilinear') 

        f4att = self.block4att(f4, f5)
        f4cat = torch.cat((f4att, f5up, f5predup), dim = 1)
        f6, f6up = self.block6(f4cat)

        f6pred = self.conv_b6(f6)
        f6predup = nn.functional.interpolate(f6pred, 
                    size = list(f3.shape)[2:], mode = 'trilinear')
        f6predup_out = nn.functional.interpolate(f6pred, 
                    size = list(x.shape)[2:], mode = 'trilinear') 

        f3att = self.block3att(f3, f6)
        f3cat = torch.cat((f3att, f6up, f6predup), dim = 1)
        f7, f7up = self.block7(f3cat)

        f7pred = self.conv_b7(f7)
        f7predup = nn.functional.interpolate(f7pred, 
                    size = list(f2.shape)[2:], mode = 'trilinear')
        f7predup_out = nn.functional.interpolate(f7pred, 
                    size = list(x.shape)[2:], mode = 'trilinear')            
        f2att = self.block2att(f2, f7)
        f2cat = torch.cat((f2att, f7up, f7predup), dim = 1)
        f8, f8up = self.block8(f2cat)

        f8pred = self.conv_b8(f8)
        f8predup = nn.functional.interpolate(f8pred, 
                    size = list(f1.shape)[2:], mode = 'trilinear')
        f8predup_out = nn.functional.interpolate(f8pred, 
                    size = list(x.shape)[2:], mode = 'trilinear') 

        f1att = self.block1att(f1, f8)
        f1cat = torch.cat((f1att, f8up, f8predup), dim = 1)
        f9, _ = self.block9(f1cat)

        output = self.conv_b9(f9)
        return output, f8predup_out, f7predup_out, f6predup_out, f5predup_out

if __name__ == "__main__":
    params = {'in_chns':4,
              'feature_chns':[2, 8, 32, 48, 64],
              'class_num': 2,
              'acti_func': 'leakyrelu',
              'leakyrelu_alpha': 0.01, 
              'dropout': True}
    Net = UNet2D5AGDSP(params)
    Net = Net.double()

    x  = np.random.rand(4, 4, 32, 96, 96)
    xt = torch.from_numpy(x)
    xt = torch.tensor(xt)
    
    y = Net(xt)
    y = y[0].detach().numpy()
    print(y.shape)
