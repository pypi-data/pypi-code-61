# -*- coding: utf-8 -*-
from __future__ import print_function, division

import torch
import torch.nn as nn
from pymic.net.net2d.unet2d_old import *

class AttentionGateBlock(nn.Module):
    def __init__(self, chns_l, chns_h):
        super(AttentionGateBlock, self).__init__()
        self.in_chns_l = chns_l # channel number of low level high-resolution features
        self.in_chns_h = chns_h # channel number of high level low-resolution features

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


class UpBlockWithAttention(nn.Module):
    """Upssampling followed by ConvBlock"""
    def __init__(self, in_channels1, in_channels2, out_channels, 
                 bilinear=True, dropout = False):
        """
        in_channels1: channel of high-level features
        in_channels2: channel of low-level features

        """
        super(UpBlockWithAttention, self).__init__()
        self.bilinear = bilinear
        self.dropout = dropout
        if bilinear:
            self.conv1x1 = nn.Conv2d(in_channels1, in_channels2, kernel_size = 1)
            self.up = nn.Upsample(scale_factor=2, mode='bilinear', align_corners=True)
        else:
            self.up = nn.ConvTranspose2d(in_channels1, in_channels2, kernel_size=2, stride=2)
        if(self.dropout):
            self.drop_layer = nn.Dropout(0.5)
        self.conv = ConvBlock(in_channels2 * 2, out_channels)
        self.ag   = AttentionGateBlock(in_channels2, in_channels1)

    def forward(self, x1, x2):
        x2at = self.ag(x2, x1)
        if self.bilinear:
            x1 = self.conv1x1(x1)
        x1 = self.up(x1)
        x = torch.cat([x2at, x1], dim=1)
        if(self.dropout):
            x = self.drop_layer(x)
        return self.conv(x)

class AttentionUNet2D(nn.Module):
    def __init__(self, params):
        super(AttentionUNet2D, self).__init__()
        self.params    = params
        self.in_chns   = self.params['in_chns']
        self.ft_chns   = self.params['feature_chns']
        self.n_class   = self.params['class_num']
        self.bilinear  = self.params['bilinear']
        self.dropout   = self.params['dropout']
        assert(len(self.ft_chns) == 5)

        self.in_conv= ConvBlock(self.in_chns, self.ft_chns[0])
        self.down1  = DownBlock(self.ft_chns[0], self.ft_chns[1])
        self.down2  = DownBlock(self.ft_chns[1], self.ft_chns[2])
        self.down3  = DownBlock(self.ft_chns[2], self.ft_chns[3])
        self.down4  = DownBlock(self.ft_chns[3], self.ft_chns[4])
        self.up1    = UpBlockWithAttention(self.ft_chns[4], self.ft_chns[3], self.ft_chns[3], dropout = self.dropout)
        self.up2    = UpBlockWithAttention(self.ft_chns[3], self.ft_chns[2], self.ft_chns[2], dropout = self.dropout)
        self.up3    = UpBlockWithAttention(self.ft_chns[2], self.ft_chns[1], self.ft_chns[1])
        self.up4    = UpBlockWithAttention(self.ft_chns[1], self.ft_chns[0], self.ft_chns[0])
    
        self.out_conv = nn.Conv2d(self.ft_chns[0], self.n_class,  
            kernel_size = 3, padding = 1)

    def forward(self, x):
        x_shape = list(x.shape)
        if(len(x_shape) == 5):
          [N, C, D, H, W] = x_shape
          new_shape = [N*D, C, H, W]
          x = torch.transpose(x, 1, 2)
          x = torch.reshape(x, new_shape)
        x0 = self.in_conv(x)
        x1 = self.down1(x0)
        x2 = self.down2(x1)
        x3 = self.down3(x2)
        x4 = self.down4(x3)
        
        x = self.up1(x4, x3)
        x = self.up2(x, x2)
        x = self.up3(x, x1)
        x = self.up4(x, x0)
        output = self.out_conv(x)

        if(len(x_shape) == 5):
            new_shape = [N, D] + list(output.shape)[1:]
            output = torch.reshape(output, new_shape)
            output = torch.transpose(output, 1, 2)
        return output
