import time
import torch
import torch.nn as nn
import numpy as np
from pymic.net2d.unet2d_covid import ASPPBlock

class GNBlock(nn.Module): # grouped convolution block
    """two convolution layers with batch norm and leaky relu"""
    def __init__(self, in_channels, out_channels, conv_g, norm_g, dropout_p):
        """
        dropout_p: probability to be zeroed
        """
        super(GNBlock, self).__init__()
        self.conv_conv = nn.Sequential(
            nn.Conv2d(in_channels, out_channels, kernel_size=3, padding=1, groups = conv_g),
            # nn.GroupNorm(norm_g, out_channels),
            nn.BatchNorm2d(out_channels),
            nn.LeakyReLU(),
            nn.Dropout(dropout_p),
            nn.Conv2d(out_channels, out_channels, kernel_size=3, padding=1, groups = conv_g),
            # nn.GroupNorm(norm_g, out_channels),
            nn.BatchNorm2d(out_channels),
            nn.LeakyReLU(),
        )
       
    def forward(self, x):
        return self.conv_conv(x)

class ConvLayer(nn.Module):
    def __init__(self, in_channels, out_channels, kernel_size):
        super(ConvLayer, self).__init__()
        padding = int((kernel_size - 1) / 2)
        self.conv = nn.Sequential(
            nn.Conv2d(in_channels, out_channels, kernel_size=kernel_size, padding=padding),
            nn.BatchNorm2d(out_channels),
            nn.LeakyReLU()
        )
       
    def forward(self, x):
        return self.conv(x)

class GNResBlock(nn.Module): # grouped convolution block
    """two convolution layers with batch norm and leaky relu"""
    def __init__(self, in_channels, out_channels, conv_g, norm_g, dropout_p):
        """
        dropout_p: probability to be zeroed
        """
        super(GNResBlock, self).__init__()
        self.conv1 = nn.Sequential(
            nn.Conv2d(in_channels, out_channels, kernel_size=3, padding=1, groups = conv_g),
            # nn.GroupNorm(norm_g, out_channels),
            nn.BatchNorm2d(out_channels),
            nn.LeakyReLU(),
            nn.Dropout(dropout_p))
        self.conv2 = nn.Sequential(
            nn.Conv2d(out_channels, out_channels, kernel_size=3, padding=1, groups = conv_g),
            # nn.GroupNorm(norm_g, out_channels),
            nn.BatchNorm2d(out_channels),
            nn.LeakyReLU())
       
    def forward(self, x):
        f1 = self.conv1(x)
        f2 = self.conv2(f1)
        return f1 + f2

def interleaved_concate(f1, f2):
    f1_shape = list(f1.shape)
    f2_shape = list(f2.shape)
    c1 = f1_shape[1]
    c2 = f2_shape[1]
    
    f1_shape_new = f1_shape[:1] + [c1, 1] + f1_shape[2:]
    f2_shape_new = f2_shape[:1] + [c2, 1] + f2_shape[2:]

    f1_reshape = torch.reshape(f1, f1_shape_new)
    f2_reshape = torch.reshape(f2, f2_shape_new)
    output     = torch.cat((f1_reshape, f2_reshape), dim = 2)
    out_shape  = f1_shape[:1] + [c1 + c2] + f1_shape[2:]
    output     = torch.reshape(output, out_shape)
    return output 

class SEBlock(nn.Module):
    def __init__(self, in_channels, r, conv_g, norm_g):
        super(SEBlock, self).__init__()

        redu_chns = int(in_channels / r)
        self.se_layers = nn.Sequential(
            nn.AdaptiveAvgPool2d(1),
            nn.Conv2d(in_channels, redu_chns, kernel_size=1, padding=0, groups = conv_g),
            # nn.GroupNorm(norm_g, redu_chns),
            nn.LeakyReLU(),
            nn.Conv2d(redu_chns, in_channels, kernel_size=1, padding=0, groups = conv_g),
            # nn.GroupNorm(norm_g, in_channels),
            nn.ReLU())
        
    def forward(self, x):
        f = self.se_layers(x)
        return f*x + x

def get_conv_block(block_name):
    if(block_name == 'GNBlock'):
        return GNBlock
    elif(block_name == "GNResBlock"):
        return GNResBlock
    else:
        raise ValueError("undefined block type {0:}".format(block_name))
        
class DownSEBlock(nn.Module):
    """Downsampling followed by ConvBlock"""
    def __init__(self, in_channels, out_channels, conv_g, norm_g, dropout_p, block_name = "GNBlock"):
        super(DownSEBlock, self).__init__()
        conv_block = get_conv_block(block_name)
        self.maxpool_conv = nn.Sequential(
            nn.MaxPool2d(2),
            conv_block(in_channels, out_channels, conv_g, norm_g, dropout_p),
            SEBlock(out_channels, 2, conv_g, norm_g)
        )

    def forward(self, x):
        return self.maxpool_conv(x)

class UpBlock(nn.Module):
    """Upssampling followed by ConvBlock"""
    def __init__(self, in_channels1, in_channels2, out_channels, conv_g, norm_g, dropout_p,
                 block_name = "GNBlock", bilinear=True):
        super(UpBlock, self).__init__()
        self.bilinear = bilinear
        if bilinear:
            self.conv1x1 = nn.Sequential(
                nn.Conv2d(in_channels1, in_channels2, kernel_size=1, groups = conv_g),
                # nn.GroupNorm(norm_g, in_channels2),
                nn.BatchNorm2d(in_channels2),
                nn.LeakyReLU())
            self.up = nn.Upsample(scale_factor=2, mode='bilinear', align_corners=True)
        else:
            self.up = nn.ConvTranspose2d(in_channels1, in_channels2, kernel_size=2, stride=2, groups = conv_g)

        conv_block = get_conv_block(block_name)
        self.conv = conv_block(in_channels2 * 2, out_channels, conv_g, norm_g, dropout_p)

    def forward(self, x1, x2):
        if self.bilinear:
            x1 = self.conv1x1(x1)
        x1 = self.up(x1)
        x  = interleaved_concate(x2, x1)
        return self.conv(x)

class UNet2D_MGSE(nn.Module):
    def __init__(self, params):
        super(UNet2D_MGSE, self).__init__()
        self.params    = params
        self.in_chns   = self.params['in_chns']
        self.ft_chns   = self.params['feature_chns']
        self.ft_group  = self.params['feature_grp']
        self.dropout   = self.params['dropout']
        self.n_class   = self.params['class_num']
        self.bilinear  = self.params['bilinear']
        self.block_type= self.params['block_type']
        
        assert(len(self.ft_chns) == 5)
        COVBlock    = get_conv_block(self.block_type)
        self.in_conv= COVBlock(self.in_chns, self.ft_chns[0],   1, self.ft_group, self.dropout[0])
        self.down1  = DownSEBlock(self.ft_chns[0], self.ft_chns[1], 1, self.ft_group, self.dropout[1], self.block_type)
        self.down2  = DownSEBlock(self.ft_chns[1], self.ft_chns[2], 1, self.ft_group, self.dropout[2], self.block_type)
        self.down3  = DownSEBlock(self.ft_chns[2], self.ft_chns[3], 1, self.ft_group, self.dropout[3], self.block_type)
        self.down4  = DownSEBlock(self.ft_chns[3], self.ft_chns[4], 1, self.ft_group, self.dropout[4], self.block_type)
        self.up1    = UpBlock(self.ft_chns[4], self.ft_chns[3], self.ft_chns[3],  self.ft_group, self.ft_group, 0.0, self.block_type)
        self.up2    = UpBlock(self.ft_chns[3], self.ft_chns[2], self.ft_chns[2],  self.ft_group, self.ft_group, 0.0, self.block_type)
        self.up3    = UpBlock(self.ft_chns[2], self.ft_chns[1], self.ft_chns[1],  self.ft_group, self.ft_group, 0.0, self.block_type)
        self.up4    = UpBlock(self.ft_chns[1], self.ft_chns[0], self.ft_chns[0],  self.ft_group, self.ft_group, 0.0, self.block_type)
    

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
        x0 = self.in_conv(x)
        x1 = self.down1(x0)
        x2 = self.down2(x1)
        x3 = self.down3(x2)
        x4 = self.down4(x3)
        x4 = self.aspp(x4) 

        x = self.up1(x4, x3)
        x = self.up2(x, x2)
        x = self.up3(x, x1)
        x = self.up4(x, x0)
        output = self.out_conv(x)

        if(len(x_shape) == 5):
            new_shape = [N, D] + list(output.shape)[1:]
            output = torch.reshape(output, new_shape)
            output = torch.transpose(output, 1, 2)

        output_list = torch.chunk(output, self.ft_group, dim = 1)    
        return output_list