# -*- coding: utf-8 -*-
from __future__ import print_function, division

import torch
import torch.nn as nn
import numpy as np
from pymic.layer.activation import get_acti_func
from pymic.layer.convolution import ConvolutionLayer
from pymic.layer.deconvolution import DeconvolutionLayer

class UNetDenseBlock(nn.Module):
    def __init__(self, in_channels, out_chnannels,
            dim, resample, acti_func, acti_func_param):
        super(UNetDenseBlock, self).__init__()
        
        self.in_chns   = in_channels
        self.out_chns  = out_chnannels
        self.dim       = dim
        self.resample  = resample  # resample should be 'down', 'up', or None
        self.acti_func = acti_func

        self.conv1 = ConvolutionLayer(in_channels,  out_chnannels,
                kernel_size = 3, padding=1, dim = self.dim, 
                acti_func=get_acti_func(acti_func, acti_func_param))
        self.conv2 = ConvolutionLayer(in_channels + out_chnannels, out_chnannels, 
                kernel_size = 3, padding=1, dim = self.dim, 
                acti_func=get_acti_func(acti_func, acti_func_param))
        self.conv3 = ConvolutionLayer(in_channels + 2* out_chnannels,  out_chnannels, 
                kernel_size = 3, padding=1, dim = self.dim, acti_func=get_acti_func(acti_func, acti_func_param))

        if(self.resample == 'down'):
            if(self.dim == 2):
                self.resample_layer = nn.MaxPool2d(kernel_size = 2, stride = 2)
            else:
                self.resample_layer = nn.MaxPool3d(kernel_size = 2, stride = 2)
        elif(self.resample == 'up'):
            self.resample_layer = DeconvolutionLayer(out_chnannels, out_chnannels, kernel_size = 2,
                    dim = self.dim, stride = 2, acti_func = get_acti_func(acti_func, acti_func_param))
        else:
            assert(self.resample == None)

    def forward(self, x):
        x_shape = list(x.shape)
        if(self.dim == 2 and len(x_shape) == 5):
            [N, C, D, H, W] = x_shape
            new_shape = [N*D, C, H, W]
            x = torch.transpose(x, 1, 2)
            x = torch.reshape(x, new_shape)
        f1    = self.conv1(x)
        f1cat = torch.cat((x, f1), dim = 1)
        f2    = self.conv2(f1cat)
        f2cat = torch.cat((x, f1, f2), dim = 1)
        output = self.conv3(f2cat)
        resample = None
        if(self.resample is not None):
            resample =  self.resample_layer(output)

        if(self.dim == 2 and len(x_shape) == 5):
            new_shape = [N, D] + list(output.shape)[1:]
            output = torch.reshape(output, new_shape)
            output = torch.transpose(output, 1, 2)
            if(resample is not None):
                resample_shape = list(resample.shape)
                new_shape = [N, D] + resample_shape[1:]
                resample = torch.reshape(resample, new_shape)
                resample = torch.transpose(resample, 1, 2)
        return output, resample

class UNet3DDeepDense(nn.Module):
    def __init__(self, params):
        super(UNet3DDeepDense, self).__init__()
        self.params = params
        self.in_chns   = self.params['in_chns']
        self.ft_chns   = self.params['feature_chns']
        self.n_class   = self.params['class_num']
        self.acti_func = self.params['acti_func']
        self.dropout   = self.params['dropout']
        self.resolution_level = len(self.ft_chns)
        assert(self.resolution_level == 5 or self.resolution_level == 4)

        self.block1 = UNetDenseBlock(self.in_chns, self.ft_chns[0], 
             3, 'down', self.acti_func, self.params)

        self.block2 = UNetDenseBlock(self.ft_chns[0], self.ft_chns[1], 
             3, 'down', self.acti_func, self.params)

        self.block3 = UNetDenseBlock(self.ft_chns[1], self.ft_chns[2], 
             3, 'down', self.acti_func, self.params)

        if(self.resolution_level == 4):
            self.block4 = UNetDenseBlock(self.ft_chns[2], self.ft_chns[3], 
             3, 'up', self.acti_func, self.params)

        if(self.resolution_level == 5):
            self.block4 = UNetDenseBlock(self.ft_chns[2], self.ft_chns[3], 
                3, 'down', self.acti_func, self.params)

            self.block5 = UNetDenseBlock(self.ft_chns[3], self.ft_chns[4], 
                3, 'up', self.acti_func, self.params)

            self.block6 = UNetDenseBlock(self.ft_chns[3] + self.ft_chns[4], self.ft_chns[3], 
                3, 'up',  self.acti_func, self.params)

        self.block7 = UNetDenseBlock(self.ft_chns[2] + self.ft_chns[3], self.ft_chns[2], 
             3, 'up', self.acti_func, self.params)

        self.block8 = UNetDenseBlock(self.ft_chns[1] + self.ft_chns[2]+ self.n_class, self.ft_chns[1], 
             3, 'up', self.acti_func, self.params)

        self.block9 = UNetDenseBlock(self.ft_chns[0] + self.ft_chns[1], self.ft_chns[0], 
             3, None, self.acti_func, self.params)

        
        if(self.dropout):
             self.drop3 = nn.Dropout(p=0.2)
             self.drop4 = nn.Dropout(p=0.2)
             if(self.resolution_level == 5):
                  self.drop5 = nn.Dropout(p=0.3)
                  
        self.conv7 = nn.Conv3d(self.ft_chns[2], self.n_class, 
            kernel_size = 3, padding = 1)

        self.conv9 = nn.Conv3d(self.ft_chns[0], self.n_class, 
            kernel_size = 3, padding = 1)

    def forward(self, x):
        f1, d1 = self.block1(x)
        f2, d2 = self.block2(d1)
        f3, d3 = self.block3(d2)
        if(self.dropout):
            d3 = self.drop3(d3)
        if(self.resolution_level == 4):
            f4, f4up = self.block4(d3)
            if(self.dropout):
                f4up = self.drop4(f4up)
            f3cat = torch.cat((f3, f4up), dim = 1)
        else:
            f4, d4 = self.block4(d3)
            if(self.dropout):
                d4 = self.drop4(d4)
            f5, f5up = self.block5(d4)
            if(self.dropout):
                 f5up = self.drop5(f5up)

            f4cat = torch.cat((f4, f5up), dim = 1)
            f6, f6up = self.block6(f4cat)

            f3cat = torch.cat((f3, f6up), dim = 1)

        f7, f7up = self.block7(f3cat)

        f7pred   = self.conv7(f7)
        f7predup = nn.functional.interpolate(f7pred, 
                    size = list(f2.shape)[2:], mode = 'trilinear')
        f7predup_out = nn.functional.interpolate(f7pred, 
                    size = list(x.shape)[2:],  mode = 'trilinear')  

        f2cat = torch.cat((f2, f7up, f7predup), dim = 1)
        f8, f8up  = self.block8(f2cat)

        f1cat = torch.cat((f1, f8up), dim = 1)
        f9, _   = self.block9(f1cat)

        output = self.conv9(f9)
        return output, f7predup_out

if __name__ == "__main__":
    params = {
              'in_chns':4,
              'feature_chns':[2, 8, 32, 48],
              'class_num': 2,
              'acti_func': 'leakyrelu',
              'dropout': True}
    Net = UNet3DDeepDense(params)
    Net = Net.double()

    x  = np.random.rand(4, 4, 64, 64, 64)
    xt = torch.from_numpy(x)
    xt = torch.tensor(xt)
    
    y0, y1 = Net(xt)
    y = y0.detach().numpy()
    print(y.shape)
