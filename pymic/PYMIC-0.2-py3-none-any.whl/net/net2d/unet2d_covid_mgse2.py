import time
import torch
import torch.nn as nn
import numpy as np
from pymic.net2d.unet2d_covid import ASPPBlock
from pymic.net2d.unet2d_covid_mgse import * 

class ConvLayer(nn.Module):
    def __init__(self, in_channels, out_channels, kernel_size = 1):
        super(ConvLayer, self).__init__()
        padding = int((kernel_size - 1) / 2)
        self.conv = nn.Sequential(
            nn.Conv2d(in_channels, out_channels, kernel_size=kernel_size, padding=padding),
            nn.BatchNorm2d(out_channels),
            nn.LeakyReLU()
        )
       
    def forward(self, x):
        return self.conv(x)

class UNet2D_MGSE2(nn.Module):
    def __init__(self, params):
        super(UNet2D_MGSE2, self).__init__()
        self.params    = params
        self.in_chns   = self.params['in_chns']
        self.ft_chns   = self.params['feature_chns']
        self.ft_group  = self.params['feature_grp']
        self.dropout   = self.params['dropout']
        self.n_class   = self.params['class_num']
        self.bilinear  = self.params['bilinear']
        self.block_type= self.params['block_type']
        
        assert(len(self.ft_chns) == 5)
        f0_half = int(self.ft_chns[0] / 2)
        f1_half = int(self.ft_chns[1] / 2)
        f2_half = int(self.ft_chns[2] / 2)
        f3_half = int(self.ft_chns[3] / 2)
        COVBlock    = get_conv_block(self.block_type)
        self.in_conv= COVBlock(self.in_chns, self.ft_chns[0],   1, self.ft_group, self.dropout[0])
        self.down1  = DownSEBlock(self.ft_chns[0], self.ft_chns[1], 1, self.ft_group, self.dropout[1], self.block_type)
        self.down2  = DownSEBlock(self.ft_chns[1], self.ft_chns[2], 1, self.ft_group, self.dropout[2], self.block_type)
        self.down3  = DownSEBlock(self.ft_chns[2], self.ft_chns[3], 1, self.ft_group, self.dropout[3], self.block_type)
        self.down4  = DownSEBlock(self.ft_chns[3], self.ft_chns[4], 1, self.ft_group, self.dropout[4], self.block_type)
        self.bridge0= ConvLayer(self.ft_chns[0], f0_half)
        self.bridge1= ConvLayer(self.ft_chns[1], f1_half)
        self.bridge2= ConvLayer(self.ft_chns[2], f2_half)
        self.bridge3= ConvLayer(self.ft_chns[3], f3_half)

        self.up1    = UpBlock(self.ft_chns[4], f3_half, self.ft_chns[3], self.ft_group, self.ft_group, 0.0, self.block_type)
        self.up2    = UpBlock(self.ft_chns[3], f2_half, self.ft_chns[2], self.ft_group, self.ft_group, 0.0, self.block_type)
        self.up3    = UpBlock(self.ft_chns[2], f1_half, self.ft_chns[1], self.ft_group, self.ft_group, 0.0, self.block_type)
        self.up4    = UpBlock(self.ft_chns[1], f0_half, self.ft_chns[0], self.ft_group, self.ft_group, 0.0, self.block_type)
    

        f4 = self.ft_chns[4]
        aspp_chns = [int(f4 / 4), int(f4 / 4), int(f4 / 4), int(f4 / 4)]
        aspp_knls = [1, 3, 3, 3]
        aspp_dila = [1, 2, 4, 6]
        self.aspp = ASPPBlock(f4, aspp_chns, aspp_knls, aspp_dila)

        self.out_conv = nn.Conv2d(self.ft_chns[0], self.n_class * self.ft_group,  
            kernel_size = 3, padding = 1, groups = self.ft_group)

    def forward(self, x):
        x_shape = list(x.shape)
        if(len(x_shape) == 5):
          [N, C, D, H, W] = x_shape
          new_shape = [N*D, C, H, W]
          x = torch.transpose(x, 1, 2)
          x = torch.reshape(x, new_shape)
        x0  = self.in_conv(x)
        x0b = self.bridge0(x0)
        x1  = self.down1(x0)
        x1b = self.bridge1(x1)
        x2  = self.down2(x1)
        x2b = self.bridge2(x2)
        x3  = self.down3(x2)
        x3b = self.bridge3(x3)
        x4  = self.down4(x3)
        x4  = self.aspp(x4) 

        x = self.up1(x4, x3b)
        x = self.up2(x, x2b)
        x = self.up3(x, x1b)
        x = self.up4(x, x0b)
        output = self.out_conv(x)

        if(len(x_shape) == 5):
            new_shape = [N, D] + list(output.shape)[1:]
            output = torch.reshape(output, new_shape)
            output = torch.transpose(output, 1, 2)

        output_list = torch.chunk(output, self.ft_group, dim = 1)    
        return output_list