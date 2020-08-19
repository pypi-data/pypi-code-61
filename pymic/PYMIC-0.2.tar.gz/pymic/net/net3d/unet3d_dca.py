# -*- coding: utf-8 -*-
from __future__ import print_function, division

import torch
import torch.nn as nn
import numpy as np
from pymic.layer.activation import get_acti_func
from pymic.layer.convolution import ConvolutionLayer
from pymic.layer.deconvolution import DeconvolutionLayer

class UNetBlock(nn.Module):
    def __init__(self,in_channels, out_channels, acti_func, acti_func_param):
        super(UNetBlock, self).__init__()
        
        self.in_chns   = in_channels
        self.out_chns  = out_channels
        self.acti_func = acti_func

        self.conv1 = ConvolutionLayer(in_channels,  out_channels, 3, 
                padding = 1, acti_func=get_acti_func(acti_func, acti_func_param))
        self.conv2 = ConvolutionLayer(out_channels, out_channels, 3, 
                padding = 1, acti_func=get_acti_func(acti_func, acti_func_param))

    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        return x

class DCABlock(nn.Module):
    def __init__(self, chns_l, chns_h):
        super(DCABlock, self).__init__()
        self.chns_l = chns_l 
        self.chns_h = chns_h
        half_chns    = int(chns_l / 2)

        self.glb_pool = nn.AdaptiveAvgPool3d(1)
        self.conv_cl_1 = nn.Conv3d(self.chns_l, half_chns,
                kernel_size = 1, bias = True)
        self.conv_cl_2 = nn.Conv3d(half_chns, self.chns_l,
                kernel_size = 1, bias = True)
        
        self.conv_ch_1 = nn.Conv3d(self.chns_h, half_chns,
                kernel_size = 1, bias = True)
        self.conv_ch_2 = nn.Conv3d(half_chns, self.chns_h,
                kernel_size = 1, bias = True)

        self.conv_s_1 = nn.Conv3d(self.chns_h, half_chns,
                kernel_size = 1, bias = True)
        self.conv_s_2 = nn.Conv3d(half_chns, 1,
                kernel_size = 3, padding = 1, bias = True)

        self.act_relu = nn.ReLU()
        self.act_sigm = nn.Sigmoid()

    def forward(self, xl, xh):
        # channel attention for xl
        a_l = self.glb_pool(xl)
        a_l = self.conv_cl_1(a_l)
        a_l = self.act_relu(a_l)
        a_l = self.conv_cl_2(a_l)
        a_l = self.act_sigm(a_l)
        xl_1 = xl * a_l
        
        a_h = self.glb_pool(xh)
        a_h = self.conv_ch_1(a_h)
        a_h = self.act_relu(a_h)
        a_h = self.conv_ch_2(a_h)
        a_h = self.act_sigm(a_h)
        xh_1 = xh * a_h

        a_s = self.conv_s_1(xh_1)
        a_s = self.act_relu(a_s)
        a_s = self.conv_s_2(a_s)
        a_s = self.act_sigm(a_s)

        x_cat0 = torch.cat((xl, xh), dim = 1)
        x_cat1 = torch.cat((xl_1, xh_1), dim = 1)
        output = x_cat0 + x_cat1 * a_s 
        return output, a_s

class DCABlockNoRes(DCABlock):
    def __init__(self, chns_l, chns_h):
        super(DCABlockNoRes, self).__init__(chns_l, chns_h)
        
    def forward(self, xl, xh):
        # channel attention for xl
        a_l = self.glb_pool(xl)
        a_l = self.conv_cl_1(a_l)
        a_l = self.act_relu(a_l)
        a_l = self.conv_cl_2(a_l)
        a_l = self.act_sigm(a_l)
        xl_1 = xl * a_l
        
        a_h = self.glb_pool(xh)
        a_h = self.conv_ch_1(a_h)
        a_h = self.act_relu(a_h)
        a_h = self.conv_ch_2(a_h)
        a_h = self.act_sigm(a_h)
        xh_1 = xh * a_h

        a_s = self.conv_s_1(xh_1)
        a_s = self.act_relu(a_s)
        a_s = self.conv_s_2(a_s)
        a_s = self.act_sigm(a_s)

        x_cat1 = torch.cat((xl_1, xh_1), dim = 1)
        output = x_cat1 * a_s 
        return output, a_s

def get_CA_block(ca_name):
    if(ca_name == "DCABlock"):
        return DCABlock
    elif(ca_name == 'DCABlockNoRes'):
        return DCABlockNoRes
    else:
        raise ValueError('undefined attention block {0:}'.format(ca_name))

class UNet3D_DCA(nn.Module):
    def __init__(self, params):
        super(UNet3D_DCA, self).__init__()
        self.params = params
        self.in_chns   = self.params['in_chns']
        self.ft_chns   = self.params['feature_chns']
        self.n_class   = self.params['class_num']
        self.acti_func = self.params['acti_func']
        self.att_name  = self.params['att_name']
        self.dropout   = self.params['dropout']
        self.ouput_att = self.params.get('output_att', False)
        self.resolution_level = len(self.ft_chns)
        assert(self.resolution_level == 5 or self.resolution_level == 4)

        self.block1 = UNetBlock(self.in_chns, self.ft_chns[0], 
             self.acti_func, self.params)

        self.block2 = UNetBlock(self.ft_chns[0], self.ft_chns[1], 
             self.acti_func, self.params)

        self.block3 = UNetBlock(self.ft_chns[1], self.ft_chns[2], 
             self.acti_func, self.params)

        self.block4 = UNetBlock(self.ft_chns[2], self.ft_chns[3], 
             self.acti_func, self.params)

        if(self.resolution_level == 5):
            self.block5 = UNetBlock(self.ft_chns[3], self.ft_chns[4], 
                 self.acti_func, self.params)

            self.block6 = UNetBlock(self.ft_chns[3] * 2, self.ft_chns[3], 
                 self.acti_func, self.params)

        self.block7 = UNetBlock(self.ft_chns[2] * 2, self.ft_chns[2], 
             self.acti_func, self.params)

        self.block8 = UNetBlock(self.ft_chns[1] * 2, self.ft_chns[1], 
             self.acti_func, self.params)

        self.block9 = UNetBlock(self.ft_chns[0] * 2, self.ft_chns[0], 
             self.acti_func, self.params)

        self.down1 = nn.MaxPool3d(kernel_size = 2)
        self.down2 = nn.MaxPool3d(kernel_size = 2)
        self.down3 = nn.MaxPool3d(kernel_size = 2)
        if(self.resolution_level == 5):
            self.down4 = nn.MaxPool3d(kernel_size = 2)

            self.up1 = DeconvolutionLayer(self.ft_chns[4], self.ft_chns[3], kernel_size = 2,
                stride = 2, acti_func = get_acti_func(self.acti_func, self.params))
        self.up2 = DeconvolutionLayer(self.ft_chns[3], self.ft_chns[2], kernel_size = 2,
            stride = 2, acti_func = get_acti_func(self.acti_func, self.params))
        self.up3 = DeconvolutionLayer(self.ft_chns[2], self.ft_chns[1], kernel_size = 2,
            stride = 2, acti_func = get_acti_func(self.acti_func, self.params))
        self.up4 = DeconvolutionLayer(self.ft_chns[1], self.ft_chns[0], kernel_size = 2,
            stride = 2, acti_func = get_acti_func(self.acti_func, self.params))

        if(self.dropout > 0.0):
             self.drop3 = nn.Dropout(self.dropout)
             self.drop4 = nn.Dropout(self.dropout)
             if(self.resolution_level == 5):
                  self.drop5 = nn.Dropout(self.dropout)
        
        ATT_Block = get_CA_block(self.att_name)
        if(self.resolution_level == 5):          
            self.ca6 = ATT_Block(self.ft_chns[3], self.ft_chns[3])
        self.ca7 = ATT_Block(self.ft_chns[2], self.ft_chns[2])
        self.ca8 = ATT_Block(self.ft_chns[1], self.ft_chns[1])
        self.ca9 = ATT_Block(self.ft_chns[0], self.ft_chns[0])

        self.conv = nn.Conv3d(self.ft_chns[0], self.n_class, 
            kernel_size = 3, padding = 1)

    def forward(self, x):
        f1 = self.block1(x)
        d1 = self.down1(f1)

        f2 = self.block2(d1)
        d2 = self.down2(f2)

        f3 = self.block3(d2)
        if(self.dropout):
             f3 = self.drop3(f3)
        d3 = self.down3(f3)

        f4 = self.block4(d3)
        if(self.dropout):
             f4 = self.drop4(f4)

        if(self.resolution_level == 5):
            d4 = self.down4(f4)
            f5 = self.block5(d4)
            if(self.dropout):
                 f5 = self.drop5(f5)

            f5up  = self.up1(f5)
            f4cat, att_s4 = self.ca6(f4, f5up)
            f6    = self.block6(f4cat)

            f6up  = self.up2(f6)
            f3cat, att_s3 = self.ca7(f3, f6up)
        else:
            f4up  = self.up2(f4)
            f3cat, att_s3 = self.ca7(f3, f4up)
        f7    = self.block7(f3cat)

        f7up  = self.up3(f7)
        f2cat, att_s2 = self.ca8(f2, f7up)
        f8    = self.block8(f2cat)
        
        f8up  = self.up4(f8)
        f1cat, att_s1 = self.ca9(f1, f8up)
        f9    = self.block9(f1cat)
        
        output = self.conv(f9)
        if(self.ouput_att):
            return att_s1
        else:
            return output

if __name__ == "__main__":
    params = {'in_chns': 1,
              'feature_chns':[8, 32, 48, 64],
              'class_num': 2,
              'att_name': 'DCABlock',
              'acti_func': 'leakyrelu',
              'leakyrelu_alpha': 0.01,
              'dropout': 0.4,
              'output_att': False}
    Net = UNet3D_DCA(params)
    Net = Net.float()
    device = torch.device('cuda:1')
    Net.to(device)

    xt = torch.randn(2, 1, 80, 80, 80)
    xt = xt.to(device)
    
    y0 = Net(xt)
    # y1 = Net(xt)[1]
    # print(len(y.size()))
    y0 = y0.detach().cpu().numpy()
    # y1 = y1.detach().cpu().numpy()
    print(y0.shape)
    # print(y1.shape)
