import time
import torch
import torch.nn as nn
import numpy as np

class GNBlock(nn.Module): # grouped convolution block
    """two convolution layers with batch norm and leaky relu"""
    def __init__(self, in_channels, out_channels, groups,  dropout_p):
        """
        dropout_p: probability to be zeroed
        """
        super(GNBlock, self).__init__()
        self.conv_conv = nn.Sequential(
            nn.Conv2d(in_channels, out_channels, kernel_size=3, padding=1, groups = groups),
            nn.GroupNorm(groups, out_channels),
            nn.LeakyReLU(),
            nn.Dropout(dropout_p),
            nn.Conv2d(out_channels, out_channels, kernel_size=3, padding=1, groups = groups),
            nn.GroupNorm(groups, out_channels),
            nn.LeakyReLU(),
        )
       
    def forward(self, x):
        return self.conv_conv(x)

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


class DownBlock(nn.Module):
    """Downsampling followed by ConvBlock"""
    def __init__(self, in_channels, out_channels, groups, dropout_p):
        super(DownBlock, self).__init__()
        self.maxpool_conv = nn.Sequential(
            nn.MaxPool2d(2),
            GNBlock(in_channels, out_channels, groups, dropout_p)
        )

    def forward(self, x):
        return self.maxpool_conv(x)

class UpBlock(nn.Module):
    """Upssampling followed by ConvBlock"""
    def __init__(self, in_channels1, in_channels2, out_channels, groups, dropout_p,
                 bilinear=True):
        super(UpBlock, self).__init__()
        self.bilinear = bilinear
        if bilinear:
            self.conv1x1 = nn.Conv2d(in_channels1, in_channels2, kernel_size = 1)
            self.up = nn.Upsample(scale_factor=2, mode='bilinear', align_corners=True)
        else:
            self.up = nn.ConvTranspose2d(in_channels1, in_channels2, kernel_size=2, stride=2)

        self.conv = GNBlock(in_channels2 * 2, out_channels, groups, dropout_p)

    def forward(self, x1, x2):
        if self.bilinear:
            x1 = self.conv1x1(x1)
        x1 = self.up(x1)
        x  = interleaved_concate(x2, x1)
        return self.conv(x)

class UNet2D_MG(nn.Module):
    def __init__(self, params):
        super(UNet2D_MG, self).__init__()
        self.params    = params
        self.in_chns   = self.params['in_chns']
        self.ft_chns   = self.params['feature_chns']
        self.ft_groups = self.params['feature_grps']
        self.dropout   = self.params['dropout']
        self.n_class   = self.params['class_num']
        self.bilinear  = self.params['bilinear']
        
        assert(len(self.ft_chns) == 5)
        self.conv0  = nn.Conv2d(self.in_chns, self.ft_groups[0],  kernel_size = 3, padding = 1)
        self.in_conv= GNBlock(self.ft_groups[0], self.ft_chns[0], self.ft_groups[0], self.dropout[0])
        self.down1  = DownBlock(self.ft_chns[0], self.ft_chns[1], self.ft_groups[1], self.dropout[1])
        self.down2  = DownBlock(self.ft_chns[1], self.ft_chns[2], self.ft_groups[2], self.dropout[2])
        self.down3  = DownBlock(self.ft_chns[2], self.ft_chns[3], self.ft_groups[3], self.dropout[3])
        self.down4  = DownBlock(self.ft_chns[3], self.ft_chns[4], self.ft_groups[4], self.dropout[4])
        self.up1    = UpBlock(self.ft_chns[4], self.ft_chns[3], self.ft_chns[3], self.ft_groups[3], self.dropout[3])
        self.up2    = UpBlock(self.ft_chns[3], self.ft_chns[2], self.ft_chns[2], self.ft_groups[2], self.dropout[2])
        self.up3    = UpBlock(self.ft_chns[2], self.ft_chns[1], self.ft_chns[1], self.ft_groups[1], self.dropout[1])
        self.up4    = UpBlock(self.ft_chns[1], self.ft_chns[0], self.ft_chns[0], self.ft_groups[0], self.dropout[0])
    
        self.out_conv = nn.Conv2d(self.ft_chns[0], self.n_class * self.ft_groups[0],  
            kernel_size = 3, padding = 1, groups = self.ft_groups[0])

    def forward(self, x):
        x_shape = list(x.shape)
        if(len(x_shape) == 5):
          [N, C, D, H, W] = x_shape
          new_shape = [N*D, C, H, W]
          x = torch.transpose(x, 1, 2)
          x = torch.reshape(x, new_shape)
        x0 = self.conv0(x)
        x0 = self.in_conv(x0)
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

        output_list = torch.chunk(output, self.ft_groups[0], dim = 1)    
        return output_list