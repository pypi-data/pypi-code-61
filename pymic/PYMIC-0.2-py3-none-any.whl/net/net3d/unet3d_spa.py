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

class AttentionGateBlock(nn.Module):
    def __init__(self, chns_l, chns_h):
        super(AttentionGateBlock, self).__init__()
        self.in_chns_l = chns_l # channel number of low level features
        self.in_chns_h = chns_h # channel number of high level features

        self.out_chns = int(min(self.in_chns_h, self.in_chns_h)/2)
        self.conv1 = nn.Conv3d(self.in_chns_h, self.out_chns,
                kernel_size = 1, bias = True)
        self.conv2 = nn.Conv3d(self.out_chns, 1,
                kernel_size = 1, bias = True)
        self.act1 = nn.ReLU()
        self.act2 = nn.Sigmoid()

    def forward(self, x_l, x_h, x_h_up):
        input_shape = list(x_l.shape)

        # get attention coefficient based on high-level feature
        att = self.conv1(x_h)
        att = self.act1(att)
        att = self.conv2(att)
        att = self.act2(att)
        # resize attention map to the shape of low-level feature
        att = nn.functional.interpolate(att, size = input_shape[2:], mode = 'trilinear')
        output = torch.cat((x_l, x_h_up), dim = 1)
        output = att * output + output
        return output, att

class SEBlock(nn.Module):
    def __init__(self, chns_in, res_connection = False):
        super(SEBlock, self).__init__()
        self.chns_in = chns_in # channel number of low level features
        self.res_connection = res_connection
        half_chns = int(chns_in / 2)
        self.glb_pool = nn.AdaptiveAvgPool3d(1)
        self.conv_1 = nn.Conv3d(self.chns_in, half_chns,
                kernel_size = 1, bias = True)
        self.conv_2 = nn.Conv3d(half_chns, self.chns_in,
                kernel_size = 1, bias = True)

        self.act1 = nn.ReLU()
        self.act2 = nn.Sigmoid()

    def forward(self, x):
        att = self.glb_pool(x)
        att = self.conv_1(att)
        att = self.act1(att)
        att = self.conv_2(att)
        att = self.act2(att)
        output = att * x
        if(self.res_connection):
            output = output + x 
        return output


class UNet3D_SPA(nn.Module):
    def __init__(self, params):
        super(UNet3D_SPA, self).__init__()
        self.params = params
        self.in_chns   = self.params['in_chns']
        self.ft_chns   = self.params['feature_chns']
        self.n_class   = self.params['class_num']
        self.acti_func = self.params['acti_func']
        self.dropout   = self.params['dropout']
        self.with_se   = self.params['with_se']
        self.deep_spv  = self.params['deep_spv']
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
                  
        self.conv = nn.Conv3d(self.ft_chns[0], self.n_class, 
            kernel_size = 3, padding = 1)
        
        if(self.deep_spv):
            self.conv8 = nn.Conv3d(self.ft_chns[1], self.n_class, 
                kernel_size = 3, padding = 1)
            self.conv7 = nn.Conv3d(self.ft_chns[2], self.n_class, 
                kernel_size = 3, padding = 1)
        
        if(self.resolution_level == 5):
            self.block4att = AttentionGateBlock(self.ft_chns[3], self.ft_chns[4])
            if(self.with_se):
                self.block4se  = SEBlock(self.ft_chns[3] * 2, self.se_res)
        self.block3att = AttentionGateBlock(self.ft_chns[2], self.ft_chns[3])
        self.block2att = AttentionGateBlock(self.ft_chns[1], self.ft_chns[2])
        self.block1att = AttentionGateBlock(self.ft_chns[0], self.ft_chns[1])
        if(self.with_se):
            self.block3se  = SEBlock(self.ft_chns[2] * 2, self.se_res)
            self.block2se  = SEBlock(self.ft_chns[1] * 2, self.se_res)
            self.block1se  = SEBlock(self.ft_chns[0] * 2, self.se_res)

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
            f4catatt, att4 = self.block4att(f4, f5, f5up)
            if(self.with_se):
                f4catatt = self.block4se(f4catatt)
            f6    = self.block6(f4catatt)

            f6up  = self.up2(f6)
            f3catatt, att3 = self.block3att(f3, f6, f6up)
            if(self.with_se):
                f3catatt = self.block3se(f3catatt)
        else:
            f4up  = self.up2(f4)
            f3catatt, att3 = self.block3att(f3, f4, f4up)
            if(self.with_se):
                f3catatt = self.block3se(f3catatt)
        f7    = self.block7(f3catatt)

        f7up  = self.up3(f7)
        f2catatt, att2 = self.block2att(f2, f7, f7up)
        if(self.with_se):
            f2catatt = self.block2se(f2catatt)
        f8    = self.block8(f2catatt)

        f8up  = self.up4(f8)
        f1catatt, att1 = self.block1att(f1, f8, f8up)
        if(self.with_se):
            f1catatt = self.block1se(f1catatt)
        f9    = self.block9(f1catatt)

        output = self.conv(f9)
        out_shape = list(output.shape)
        if(self.deep_spv):
            pred8 = self.conv8(f8)
            pred7 = self.conv7(f7)
            pred8up = nn.functional.interpolate(pred8, size = out_shape[2:], mode = 'trilinear')
            pred7up = nn.functional.interpolate(pred7, size = out_shape[2:], mode = 'trilinear')

        # get average att
        att3_up = nn.functional.interpolate(att3, size = out_shape[2:], mode = 'trilinear')
        att2_up = nn.functional.interpolate(att2, size = out_shape[2:], mode = 'trilinear')
        avg_att = (att1 + att2_up + att3_up) / 3
        # prob_att = torch.cat((1 - avg_att, avg_att), dim = 1)
        # prob_att = 
        if(self.ouput_att):
            return att1
        else:
            if(self.deep_spv):
                return output, pred8up, pred7up
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
