# -*- coding: utf-8 -*-
from __future__ import print_function, division

import torch
import torch.nn as nn
from pymic.net.net2d.unet2d import ConvBlock, DownBlock, UpBlock

class ASPPBlock(nn.Module):
    """two convolution layers with batch norm and leaky relu"""
    def __init__(self,in_channels, out_channels_list, kernel_size_list, dilation_list):
        super(ASPPBlock, self).__init__()
        self.conv_num = len(out_channels_list)
        assert(self.conv_num == 4)
        assert(self.conv_num == len(kernel_size_list) and self.conv_num == len(dilation_list))
        pad0 = int((kernel_size_list[0] - 1) / 2 * dilation_list[0])
        pad1 = int((kernel_size_list[1] - 1) / 2 * dilation_list[1])
        pad2 = int((kernel_size_list[2] - 1) / 2 * dilation_list[2])
        pad3 = int((kernel_size_list[3] - 1) / 2 * dilation_list[3])
        self.conv_1 = nn.Conv2d(in_channels, out_channels_list[0], kernel_size = kernel_size_list[0], 
                    dilation = dilation_list[0], padding = pad0 )
        self.conv_2 = nn.Conv2d(in_channels, out_channels_list[1], kernel_size = kernel_size_list[1], 
                    dilation = dilation_list[1], padding = pad1 )
        self.conv_3 = nn.Conv2d(in_channels, out_channels_list[2], kernel_size = kernel_size_list[2], 
                    dilation = dilation_list[2], padding = pad2 )
        self.conv_4 = nn.Conv2d(in_channels, out_channels_list[3], kernel_size = kernel_size_list[3], 
                    dilation = dilation_list[3], padding = pad3 )

        out_channels = out_channels_list[0] + out_channels_list[1] + out_channels_list[2] + out_channels_list[3] 
        self.conv_1x1 = nn.Sequential(
            nn.Conv2d(out_channels, out_channels, kernel_size=1, padding=0),
            nn.BatchNorm2d(out_channels),
            nn.LeakyReLU())
       
    def forward(self, x):
        x1 = self.conv_1(x)
        x2 = self.conv_2(x)
        x3 = self.conv_3(x)
        x4 = self.conv_4(x)

        y = torch.cat([x1, x2, x3, x4], dim=1)
        y = self.conv_1x1(y)
        return y


class SEBlock(nn.Module):
    def __init__(self, in_channels, r):
        super(SEBlock, self).__init__()

        redu_chns = int(in_channels / r)
        self.se_layers = nn.Sequential(
            nn.AdaptiveAvgPool2d(1),
            nn.Conv2d(in_channels, redu_chns, kernel_size=1, padding=0),
            nn.LeakyReLU(),
            nn.Conv2d(redu_chns, in_channels, kernel_size=1, padding=0),
            nn.Sigmoid())
        
    def forward(self, x):
        f = self.se_layers(x)
        return f*x + x

class UNet2D_COVID(nn.Module):
    def __init__(self, params):
        super(UNet2D_COVID, self).__init__()
        self.params    = params
        self.in_chns   = self.params['in_chns']
        self.ft_chns   = self.params['feature_chns']
        self.n_class   = self.params['class_num']
        self.bilinear  = self.params['bilinear']
        self.dropout   = self.params['dropout']
        self.use_se    = self.params['use_se']
        assert(len(self.ft_chns) == 5)

        self.in_conv= ConvBlock(self.in_chns, self.ft_chns[0])
        self.down1  = DownBlock(self.ft_chns[0], self.ft_chns[1])
        self.down2  = DownBlock(self.ft_chns[1], self.ft_chns[2])
        self.down3  = DownBlock(self.ft_chns[2], self.ft_chns[3])
        self.down4  = DownBlock(self.ft_chns[3], self.ft_chns[4])
        self.up1    = UpBlock(self.ft_chns[4], self.ft_chns[3], self.ft_chns[3], dropout = self.dropout)
        self.up2    = UpBlock(self.ft_chns[3], self.ft_chns[2], self.ft_chns[2], dropout = self.dropout)
        self.up3    = UpBlock(self.ft_chns[2], self.ft_chns[1], self.ft_chns[1])
        self.up4    = UpBlock(self.ft_chns[1], self.ft_chns[0], self.ft_chns[0])

        if(self.use_se):
            self.in_se = SEBlock(self.ft_chns[0], 2)
            self.d1_se = SEBlock(self.ft_chns[1], 2)
            self.d2_se = SEBlock(self.ft_chns[2], 2)
            self.d3_se = SEBlock(self.ft_chns[3], 2)
            self.d4_se = SEBlock(self.ft_chns[4], 2)
            self.u1_se = SEBlock(self.ft_chns[3], 2)
            self.u2_se = SEBlock(self.ft_chns[2], 2)
            self.u3_se = SEBlock(self.ft_chns[1], 2)
            self.u4_se = SEBlock(self.ft_chns[0], 2)

        f4 = self.ft_chns[4]
        aspp_chns = [int(f4 / 4), int(f4 / 4), int(f4 / 4), int(f4 / 4)]
        aspp_knls = [1, 3, 3, 3]
        aspp_dila = [1, 2, 4, 6]
        self.aspp = ASPPBlock(f4, aspp_chns, aspp_knls, aspp_dila)
        
            
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
        if(self.use_se):
            x0 = self.in_se(x0)
        x1 = self.down1(x0)
        if(self.use_se):
            x1 = self.d1_se(x1)
        x2 = self.down2(x1)
        if(self.use_se):
            x2 = self.d2_se(x2)
        x3 = self.down3(x2)
        if(self.use_se):
            x3 = self.d3_se(x3)
        x4 = self.down4(x3)
        if(self.use_se):
            x4 = self.d4_se(x4)

        x4 = self.aspp(x4)
        x = self.up1(x4, x3)
        if(self.use_se):
            x = self.u1_se(x)
        x = self.up2(x, x2)
        if(self.use_se):
            x = self.u2_se(x)
        x = self.up3(x, x1)
        if(self.use_se):
            x = self.u3_se(x)
        x = self.up4(x, x0)
        if(self.use_se):
            x = self.u4_se(x)

        output = self.out_conv(x)

        if(len(x_shape) == 5):
            new_shape = [N, D] + list(output.shape)[1:]
            output = torch.reshape(output, new_shape)
            output = torch.transpose(output, 1, 2)
        return output
