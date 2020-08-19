# -*- coding: utf-8 -*-
from __future__ import print_function, division

import torch
import torch.nn as nn
from pymic.net.net2d.unet2d_covid import SEBlock, ASPPBlock

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


class SEBlock(nn.Module):
    def __init__(self, in_channels, r):
        super(SEBlock, self).__init__()

        redu_chns = int(in_channels / r)
        self.se_layers = nn.Sequential(
            nn.AdaptiveAvgPool2d(1),
            nn.Conv2d(in_channels, redu_chns, kernel_size=1, padding=0),
            nn.LeakyReLU(),
            nn.Conv2d(redu_chns, in_channels, kernel_size=1, padding=0),
            nn.ReLU())
        
    def forward(self, x):
        f = self.se_layers(x)
        return f*x + x

class ConvBNActBlock(nn.Module):
    """two convolution layers with batch norm and leaky relu"""
    def __init__(self,in_channels, out_channels, dropout_p):
        """
        dropout_p: probability to be zeroed
        """
        super(ConvBNActBlock, self).__init__()
        self.conv_conv = nn.Sequential(
            nn.Conv2d(in_channels, out_channels, kernel_size=3, padding=1),
            nn.BatchNorm2d(out_channels),
            nn.LeakyReLU(),
            nn.Dropout(dropout_p),
            nn.Conv2d(out_channels, out_channels, kernel_size=3, padding=1),
            nn.BatchNorm2d(out_channels),
            nn.LeakyReLU(),
            SEBlock(out_channels, 2)
        )
       
    def forward(self, x):
        return self.conv_conv(x)

class DownBlock(nn.Module):
    """Downsampling followed by ConvBlock"""
    def __init__(self, in_channels, out_channels, dropout_p, dual_pool = True):
        super(DownBlock, self).__init__()
        self.dual_pool = dual_pool
        self.maxpool = nn.MaxPool2d(2)
        self.avgpool = nn.AvgPool2d(2)
        in_chans = 2 * in_channels if self.dual_pool else in_channels
        self.conv = ConvBNActBlock(in_chans, out_channels, dropout_p)
        
    def forward(self, x):
        if(self.dual_pool):
            x_max = self.maxpool(x)
            x_avg = self.avgpool(x)
            x_cat = torch.cat([x_max, x_avg], dim=1)
            y = self.conv(x_cat)
            return y + x_cat
        else:
            x_max = self.maxpool(x)
            y = self.conv(x_max)
            return y 


class UpBlock(nn.Module):
    """Upsampling followed by ConvBlock"""
    def __init__(self, in_channels1, in_channels2, out_channels, 
                 bilinear=True, dropout_p = 0.5, res = True):
        super(UpBlock, self).__init__()
        self.bilinear = bilinear
        self.res = res
        if bilinear:
            self.conv1x1 = nn.Conv2d(in_channels1, in_channels2, kernel_size = 1)
            self.up = nn.Upsample(scale_factor=2, mode='bilinear', align_corners=True)
        else:
            self.up = nn.ConvTranspose2d(in_channels1, in_channels2, kernel_size=2, stride=2)
        self.conv = ConvBNActBlock(in_channels2 * 2, out_channels, dropout_p)

    def forward(self, x1, x2):
        if self.bilinear:
            x1 = self.conv1x1(x1)
        x1    = self.up(x1)
        x_cat = torch.cat([x2, x1], dim=1)
        y     = self.conv(x_cat)
        if(self.res):
            y = y + x_cat
        return y


class UNet2D_COVIDV3(nn.Module):
    """
    variant of UNet2D_COVIDV2: without aspp
    """
    def __init__(self, params):
        super(UNet2D_COVIDV3, self).__init__()
        self.params    = params
        self.in_chns   = self.params['in_chns']
        self.ft_chns   = self.params['feature_chns']
        self.n_class   = self.params['class_num']
        self.bilinear  = self.params['bilinear']
        self.dropout   = self.params['dropout']
        assert(len(self.ft_chns) == 5)

        f0_half = int(self.ft_chns[0] / 2)
        f1_half = int(self.ft_chns[1] / 2)
        f2_half = int(self.ft_chns[2] / 2)
        f3_half = int(self.ft_chns[3] / 2)
        self.in_conv= ConvBNActBlock(self.in_chns, self.ft_chns[0], self.dropout[0])
        self.down1  = DownBlock(self.ft_chns[0], self.ft_chns[1], self.dropout[1])
        self.down2  = DownBlock(self.ft_chns[1], self.ft_chns[2], self.dropout[2])
        self.down3  = DownBlock(self.ft_chns[2], self.ft_chns[3], self.dropout[3])
        self.down4  = DownBlock(self.ft_chns[3], self.ft_chns[4], self.dropout[4])
        
        self.bridge0= ConvLayer(self.ft_chns[0], f0_half)
        self.bridge1= ConvLayer(self.ft_chns[1], f1_half)
        self.bridge2= ConvLayer(self.ft_chns[2], f2_half)
        self.bridge3= ConvLayer(self.ft_chns[3], f3_half)

        self.up1    = UpBlock(self.ft_chns[4], f3_half, self.ft_chns[3], dropout_p = self.dropout[3])
        self.up2    = UpBlock(self.ft_chns[3], f2_half, self.ft_chns[2], dropout_p = self.dropout[2])
        self.up3    = UpBlock(self.ft_chns[2], f1_half, self.ft_chns[1], dropout_p = self.dropout[1])
        self.up4    = UpBlock(self.ft_chns[1], f0_half, self.ft_chns[0], dropout_p = self.dropout[0])

        # f4 = self.ft_chns[4]
        # aspp_chns = [int(f4 / 4), int(f4 / 4), int(f4 / 4), int(f4 / 4)]
        # aspp_knls = [1, 3, 3, 3]
        # aspp_dila = [1, 2, 4, 6]
        # self.aspp = ASPPBlock(f4, aspp_chns, aspp_knls, aspp_dila)
        
            
        self.out_conv = nn.Conv2d(self.ft_chns[0], self.n_class,  
            kernel_size = 3, padding = 1)

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
        # x4  = self.aspp(x4) 

        x = self.up1(x4, x3b)
        x = self.up2(x, x2b)
        x = self.up3(x, x1b)
        x = self.up4(x, x0b)
        output = self.out_conv(x)

        if(len(x_shape) == 5):
            new_shape = [N, D] + list(output.shape)[1:]
            output = torch.reshape(output, new_shape)
            output = torch.transpose(output, 1, 2)
        return output

class UNet2D_COVIDV4(nn.Module):
    """
    variant of UNet2D_COVIDV2: without bridge connection
    """
    def __init__(self, params):
        super(UNet2D_COVIDV4, self).__init__()
        self.params    = params
        self.in_chns   = self.params['in_chns']
        self.ft_chns   = self.params['feature_chns']
        self.n_class   = self.params['class_num']
        self.bilinear  = self.params['bilinear']
        self.dropout   = self.params['dropout']
        assert(len(self.ft_chns) == 5)

        f0_half = int(self.ft_chns[0] / 2)
        f1_half = int(self.ft_chns[1] / 2)
        f2_half = int(self.ft_chns[2] / 2)
        f3_half = int(self.ft_chns[3] / 2)
        self.in_conv= ConvBNActBlock(self.in_chns, self.ft_chns[0], self.dropout[0])
        self.down1  = DownBlock(self.ft_chns[0], self.ft_chns[1], self.dropout[1])
        self.down2  = DownBlock(self.ft_chns[1], self.ft_chns[2], self.dropout[2])
        self.down3  = DownBlock(self.ft_chns[2], self.ft_chns[3], self.dropout[3])
        self.down4  = DownBlock(self.ft_chns[3], self.ft_chns[4], self.dropout[4])
        
        # self.bridge0= ConvLayer(self.ft_chns[0], f0_half)
        # self.bridge1= ConvLayer(self.ft_chns[1], f1_half)
        # self.bridge2= ConvLayer(self.ft_chns[2], f2_half)
        # self.bridge3= ConvLayer(self.ft_chns[3], f3_half)

        self.up1    = UpBlock(self.ft_chns[4], self.ft_chns[3], self.ft_chns[3], 
                            dropout_p = self.dropout[3], res = False)
        self.up2    = UpBlock(self.ft_chns[3], self.ft_chns[2], self.ft_chns[2], 
                            dropout_p = self.dropout[2], res = False)
        self.up3    = UpBlock(self.ft_chns[2], self.ft_chns[1], self.ft_chns[1], 
                            dropout_p = self.dropout[1], res = False)
        self.up4    = UpBlock(self.ft_chns[1], self.ft_chns[0], self.ft_chns[0], 
                            dropout_p = self.dropout[0], res = False)

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
        x0  = self.in_conv(x)
        # x0b = self.bridge0(x0)
        x1  = self.down1(x0)
        # x1b = self.bridge1(x1)
        x2  = self.down2(x1)
        # x2b = self.bridge2(x2)
        x3  = self.down3(x2)
        # x3b = self.bridge3(x3)
        x4  = self.down4(x3)
        x4  = self.aspp(x4) 

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

class UNet2D_COVIDV5(nn.Module):
    """
    variant of UNet2D_COVIDV2: without dual pooling
    """
    def __init__(self, params):
        super(UNet2D_COVIDV5, self).__init__()
        self.params    = params
        self.in_chns   = self.params['in_chns']
        self.ft_chns   = self.params['feature_chns']
        self.n_class   = self.params['class_num']
        self.bilinear  = self.params['bilinear']
        self.dropout   = self.params['dropout']
        assert(len(self.ft_chns) == 5)

        f0_half = int(self.ft_chns[0] / 2)
        f1_half = int(self.ft_chns[1] / 2)
        f2_half = int(self.ft_chns[2] / 2)
        f3_half = int(self.ft_chns[3] / 2)
        self.in_conv= ConvBNActBlock(self.in_chns, self.ft_chns[0], self.dropout[0])
        self.down1  = DownBlock(self.ft_chns[0], self.ft_chns[1], self.dropout[1], dual_pool= False)
        self.down2  = DownBlock(self.ft_chns[1], self.ft_chns[2], self.dropout[2], dual_pool= False)
        self.down3  = DownBlock(self.ft_chns[2], self.ft_chns[3], self.dropout[3], dual_pool= False)
        self.down4  = DownBlock(self.ft_chns[3], self.ft_chns[4], self.dropout[4], dual_pool= False)
        
        self.bridge0= ConvLayer(self.ft_chns[0], f0_half)
        self.bridge1= ConvLayer(self.ft_chns[1], f1_half)
        self.bridge2= ConvLayer(self.ft_chns[2], f2_half)
        self.bridge3= ConvLayer(self.ft_chns[3], f3_half)

        self.up1    = UpBlock(self.ft_chns[4], f3_half, self.ft_chns[3], dropout_p = self.dropout[3])
        self.up2    = UpBlock(self.ft_chns[3], f2_half, self.ft_chns[2], dropout_p = self.dropout[2])
        self.up3    = UpBlock(self.ft_chns[2], f1_half, self.ft_chns[1], dropout_p = self.dropout[1])
        self.up4    = UpBlock(self.ft_chns[1], f0_half, self.ft_chns[0], dropout_p = self.dropout[0])

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
        return output