# -*- coding: utf-8 -*-
from __future__ import print_function, division

import time
import torch
import torch.nn as nn
import numpy as np
from pymic.layer.activation import get_acti_func
from pymic.layer.convolution import ConvolutionLayer, DepthSeperableConvolutionLayer
from pymic.layer.deconvolution import DeconvolutionLayer, DepthSeperableDeconvolutionLayer
from pymic.net3d.unet3d_blocks import *

def channel_shuffle(x, groups):
    data_shape = x.data.size()
    channels_per_group  = data_shape[1] // groups

    # reshape
    if(len(data_shape) == 4):
        x = x.view(data_shape[0], groups, channels_per_group, data_shape[2], data_shape[3])
    else:
        x = x.view(data_shape[0], groups, channels_per_group, data_shape[2], data_shape[3], data_shape[4])
    x = torch.transpose(x, 1, 2).contiguous() 

    # flatten
    if(len(data_shape) == 4):
        x = x.view(data_shape[0], -1, data_shape[2], data_shape[3])
    else:
        x = x.view(data_shape[0], -1, data_shape[2], data_shape[3], data_shape[4])
    return x 

class UNetBlock(nn.Module):
    def __init__(self, dim, in_channels, out_channels, norm_type, groups, acti_func, acti_func_param):
        super(UNetBlock, self).__init__()
        self.dim       = dim
        self.in_chns   = in_channels
        self.out_chns  = out_channels
        self.acti_func = acti_func

        self.conv1 = ConvolutionLayer(in_channels,  out_channels, 3, 
                dim = self.dim, padding = 1, conv_group = groups, norm_type = norm_type, norm_group = groups,
                acti_func=get_acti_func(acti_func, acti_func_param))
        self.conv2 = ConvolutionLayer(out_channels, out_channels, 3, 
                dim = self.dim, padding = 1, conv_group = groups, norm_type = norm_type, norm_group = groups,
                acti_func=get_acti_func(acti_func, acti_func_param))

    def forward(self, x):
        f1 = self.conv1(x)
        f2 = self.conv2(f1)
        return f2


class UNetBlock_DW(nn.Module):
    """UNet block with depthwise seperable convolution
    """
    def __init__(self, dim, in_channels, out_channels, norm_type, groups, acti_func, acti_func_param):
        super(UNetBlock_DW, self).__init__()
        self.dim       = dim 
        self.in_chns   = in_channels
        self.out_chns  = out_channels
        self.acti_func = acti_func
        self.groups    = groups

        self.conv1 = DepthSeperableConvolutionLayer(in_channels, out_channels, 3, 
                dim = self.dim, padding = 1, conv_group = groups, norm_type = norm_type, norm_group = groups,
                acti_func=get_acti_func(acti_func, acti_func_param))
        self.conv2 = DepthSeperableConvolutionLayer(out_channels, out_channels, 3, 
                dim = self.dim, padding = 1, conv_group = groups, norm_type = norm_type, norm_group = groups,
                acti_func=get_acti_func(acti_func, acti_func_param))
       
    def forward(self, x):
        f1 = self.conv1(x)
        f2 = self.conv2(f1)
        return f2


class UNetBlock_DW_CF(UNetBlock_DW):
    """UNet block with depthwise seperable convolution
    """
    def __init__(self, dim, in_channels, out_channels, norm_type, groups, acti_func, acti_func_param):
        super(UNetBlock_DW_CF, self).__init__(dim, in_channels, out_channels, norm_type, groups, acti_func, acti_func_param)
       
    def forward(self, x):
        f1 = self.conv1(x)
        if(self.groups > 1):
            f1 = channel_shuffle(f1, groups = self.groups)
        f2 = self.conv2(f1)
        if(self.groups > 1):
            f2 = channel_shuffle(f2, groups = int(self.out_chns / self.groups))
        return f2

class UNetBlock_DW_CF_Res(UNetBlock_DW):
    """UNet block with depthwise seperable convolution
    """
    def __init__(self, dim, in_channels, out_channels, norm_type, groups, acti_func, acti_func_param):
        super(UNetBlock_DW_CF_Res, self).__init__(dim, in_channels, out_channels, norm_type, groups, acti_func, acti_func_param)
       
    def forward(self, x):
        f1 = self.conv1(x)
        if(self.groups > 1):
            f1 = channel_shuffle(f1, groups = self.groups)
        f2 = self.conv2(f1)
        if(self.groups > 1):
            f2 = channel_shuffle(f2, groups = int(self.out_chns / self.groups))
        return f1 + f2

class VanillaBlock(nn.Module):
    def __init__(self, dim, in_channels, out_channels, norm_type, groups, acti_func, acti_func_param):
        super(VanillaBlock, self).__init__()
        
        self.dim       = dim 
        self.in_chns   = in_channels
        self.out_chns  = out_channels
        self.acti_func = acti_func

        group1 = 1 if (in_channels < 8) else groups
        self.conv1 = ConvolutionLayer(in_channels,  out_channels, 1, 
                dim = self.dim, padding = 0, conv_group = group1, norm_type = norm_type, norm_group = group1,
                acti_func=get_acti_func(acti_func, acti_func_param))
        self.conv2 = ConvolutionLayer(out_channels, out_channels, 3, 
                dim = self.dim, padding = 1, conv_group = groups, norm_type = norm_type, norm_group = groups,
                acti_func=get_acti_func(acti_func, acti_func_param))
        self.conv3 = ConvolutionLayer(out_channels, out_channels, 3, 
                dim = self.dim, padding = 1, conv_group = groups, norm_type = norm_type, norm_group = groups,
                acti_func=get_acti_func(acti_func, acti_func_param))

    def forward(self, x):
        f1 = self.conv1(x)
        f2 = self.conv2(f1)
        f3 = self.conv3(f2)
        return f3

class ResBlock(VanillaBlock):
    def __init__(self, dim, in_channels, out_channels, norm_type, groups, acti_func, acti_func_param):
        super(ResBlock, self).__init__(dim, in_channels, out_channels, norm_type, groups, acti_func, acti_func_param)

    def forward(self, x):
        f1 = self.conv1(x)
        f2 = self.conv2(f1)
        f3 = self.conv3(f2)
        return f1 + f3

class ResBlock_DW(nn.Module):
    """UNet block with depthwise seperable convolution
    """
    def __init__(self, dim, in_channels, out_channels, norm_type, groups, acti_func, acti_func_param):
        super(ResBlock_DW, self).__init__()
        self.dim       = dim 
        self.in_chns   = in_channels
        self.out_chns  = out_channels
        self.acti_func = acti_func
        self.groups    = groups

        self.conv1 = ConvolutionLayer(in_channels,  out_channels, 1, 
                dim = self.dim, padding = 0, conv_group = 1, norm_type = norm_type, norm_group = 1,
                acti_func=get_acti_func(acti_func, acti_func_param))
        self.conv2 = DepthSeperableConvolutionLayer(out_channels, out_channels, 3, 
                dim = self.dim, padding = 1, conv_group = groups, norm_type = norm_type, norm_group = groups,
                acti_func=get_acti_func(acti_func, acti_func_param))
        self.conv3 = DepthSeperableConvolutionLayer(out_channels, out_channels, 3, 
                dim = self.dim, padding = 1, conv_group = groups, norm_type = norm_type, norm_group = groups,
                acti_func=get_acti_func(acti_func, acti_func_param))
       
    def forward(self, x):
        f1 = self.conv1(x)
        f2 = self.conv2(f1)
        f3 = self.conv3(f2)
        return f1 + f3

class ResBlock_DWGC_CF(nn.Module):
    """UNet block with depthwise seperable convolution and group convolution + channel shuffle
    """
    def __init__(self, dim, in_channels, out_channels, norm_type, groups, acti_func, acti_func_param):
        super(ResBlock_DWGC_CF, self).__init__()
        self.dim       = dim 
        self.in_chns   = in_channels
        self.out_chns  = out_channels
        self.acti_func = acti_func
        self.groups    = groups
        groups2        = int(out_channels / groups)
        self.conv1 = ConvolutionLayer(in_channels,  out_channels, 1, 
                dim = self.dim, padding = 0, conv_group = 1, norm_type = norm_type, norm_group = 1,
                acti_func=get_acti_func(acti_func, acti_func_param))
        self.conv2 = DepthSeperableConvolutionLayer(out_channels, out_channels, 3, 
                dim = self.dim, padding = 1, conv_group = groups, norm_type = norm_type, norm_group = groups,
                acti_func=get_acti_func(acti_func, acti_func_param))
        self.conv3 = DepthSeperableConvolutionLayer(out_channels, out_channels, 3, 
                dim = self.dim, padding = 1, conv_group = groups2, norm_type = norm_type, norm_group = groups2,
                acti_func=get_acti_func(acti_func, acti_func_param))

    def forward(self, x):
        f1 = self.conv1(x)
        f2 = self.conv2(f1)
        if(self.groups > 1):
            f2 = channel_shuffle(f2, groups = self.groups)
        f3 = self.conv3(f2)
        if(self.groups > 1):
            f3 = channel_shuffle(f3, groups = int(self.out_chns / self.groups))
        return f1 + f3

class PEBlock(nn.Module):
    def __init__(self, dim, channels, acti_func, acti_func_param):
        super(PEBlock, self).__init__()
        self.dim       = dim 
        self.channels  = channels
        self.acti_func = acti_func

        self.conv1 = ConvolutionLayer(channels,  int(channels / 2), 1, 
                dim = self.dim, padding = 0, conv_group = 1, norm_type = None, norm_group = 1,
                acti_func=get_acti_func(acti_func, acti_func_param))
        self.conv2 = ConvolutionLayer(int(channels / 2),  channels, 1, 
                dim = self.dim, padding = 0, conv_group = 1, norm_type = None, norm_group = 1,
                acti_func=nn.Sigmoid())

    def forward(self, x):
        # projection along each dimension
        x_shape = list(x.shape) 
        [N, C, H, W] = x_shape
        p_w = torch.sum(x, dim = -1, keepdim = True) / W  # the shape becomes [N, C, H, 1]
        p_h = torch.sum(x, dim = -2, keepdim = True) / H  # the shape becomes [N, C, 1, W]
        p_w_repeat = p_w.repeat(1, 1, 1, W)               # the shape is [N, C, H, W]
        p_h_repeat = p_h.repeat(1, 1, H, 1)               # the shape is [N, C, H, W]
        f = p_w_repeat + p_h_repeat
        f = self.conv1(f)
        f = self.conv2(f)                                 # get attention coefficient 
        out = f*x + x                                     # use a residual connection
        return out
    
class ResBlock_DWGC_CF_PE(ResBlock_DW):
    """UNet block with depthwise seperable convolution and group convolution + channel shuffle
    """
    def __init__(self, dim, in_channels, out_channels, norm_type, groups, acti_func, acti_func_param):
        super(ResBlock_DWGC_CF_PE, self).__init__(dim, in_channels, out_channels, 
            norm_type, groups, acti_func, acti_func_param)
        self.pe_block = PEBlock(dim, out_channels, acti_func, acti_func_param)
       
    def forward(self, x):
        f1 = self.conv1(x)
        if(self.groups > 1):
            f1 = channel_shuffle(f1, groups = self.groups)
        f2 = self.conv2(f1)
        f3 = self.conv3(f2)
        if(self.groups > 1):
            f3 = channel_shuffle(f3, groups = self.groups)
        out = f1 + f3
        out = self.pe_block(out)
        return out
    

class UNetND_Extention(nn.Module):
    def __init__(self, params):
        super(UNetND_Extention, self).__init__()
        self.params = params
        self.dimension = self.params['dimension']
        self.in_chns   = self.params['in_chns']
        self.ft_chns   = self.params['feature_chns']
        self.ft_groups = self.params['feature_grps']
        self.norm_type = self.params['norm_type']
        self.block_type= self.params['block_type']
        self.n_class   = self.params['class_num']
        self.acti_func = self.params['acti_func']
        self.dropout   = self.params['dropout']
        self.depth_sep_deconv= self.params['depth_sep_deconv']
        self.deep_spv  = self.params['deep_supervision']
        self.pe_block  = self.params.get('pe_block', False)
        self.resolution_level = len(self.ft_chns)
        assert(self.resolution_level == 5 or self.resolution_level == 4)
        self.construct_network()

    def get_unet_block(self, block_type):
        if(block_type == "UNetBlock"):
            return UNetBlock
        elif(block_type == 'UNetBlock_SpatialSep'):
            return UNetBlock_SpatialSep
        elif(block_type == 'UNetBlock_SpatialDepthSep'):
            return UNetBlock_SpatialDepthSep
        elif(block_type == 'UNetBlock_SpatialDepthSep2'):
            return UNetBlock_SpatialDepthSep2
        elif(block_type == 'UNetBlock_SpatialDepthSep3'):
            return UNetBlock_SpatialDepthSep3
        elif(block_type == "UNetBlock_DW"):
            return UNetBlock_DW
        elif(block_type == "UNetBlock_DW_CF"):
            return UNetBlock_DW_CF
        elif(block_type == "UNetBlock_DW_CF_Res"):
            return UNetBlock_DW_CF_Res
        else:
            raise ValueError("undefined type name {0:}".format(block_type))

    def get_deconv_layer(self, depth_sep_deconv):
        if(depth_sep_deconv):
            return DepthSeperableDeconvolutionLayer
        else:
            return DeconvolutionLayer

    def construct_network(self):
        Block = self.get_unet_block(self.block_type)
        self.block1 = Block(self.dimension, self.in_chns, self.ft_chns[0], 
            self.norm_type, self.ft_groups[0], self.acti_func, self.params)

        self.block2 = Block(self.dimension, self.ft_chns[0], self.ft_chns[1], 
            self.norm_type, self.ft_groups[1], self.acti_func, self.params)

        self.block3 = Block(self.dimension, self.ft_chns[1], self.ft_chns[2], 
            self.norm_type, self.ft_groups[2], self.acti_func, self.params)

        self.block4 = Block(self.dimension, self.ft_chns[2], self.ft_chns[3], 
            self.norm_type, self.ft_groups[3], self.acti_func, self.params)

        if(self.resolution_level == 5):
            self.block5 = Block(self.dimension, self.ft_chns[3], self.ft_chns[4], 
                self.norm_type, self.ft_groups[4], self.acti_func, self.params)

            self.block6 = Block(self.dimension, self.ft_chns[3] * 2, self.ft_chns[3],   
                self.norm_type, self.ft_groups[3], self.acti_func, self.params)

        self.block7 = Block(self.dimension, self.ft_chns[2] * 2, self.ft_chns[2], 
            self.norm_type, self.ft_groups[2], self.acti_func, self.params)

        self.block8 = Block(self.dimension, self.ft_chns[1] * 2, self.ft_chns[1], 
            self.norm_type, self.ft_groups[1], self.acti_func, self.params)

        self.block9 = Block(self.dimension, self.ft_chns[0] * 2, self.ft_chns[0], 
            self.norm_type, self.ft_groups[0], self.acti_func, self.params)

        if(self.pe_block):
            self.pe1 = PEBlock(self.dimension, self.ft_chns[0], self.acti_func, self.params)
            self.pe2 = PEBlock(self.dimension, self.ft_chns[1], self.acti_func, self.params)
            self.pe3 = PEBlock(self.dimension, self.ft_chns[2], self.acti_func, self.params)
            self.pe4 = PEBlock(self.dimension, self.ft_chns[3], self.acti_func, self.params)
            self.pe7 = PEBlock(self.dimension, self.ft_chns[2], self.acti_func, self.params)
            self.pe8 = PEBlock(self.dimension, self.ft_chns[1], self.acti_func, self.params)
            self.pe9 = PEBlock(self.dimension, self.ft_chns[0], self.acti_func, self.params)
            if(self.resolution_level == 5):
                self.pe5 = PEBlock(self.dimension, self.ft_chns[4], self.acti_func, self.params)
                self.pe6 = PEBlock(self.dimension, self.ft_chns[3], self.acti_func, self.params)

        if(self.dimension == 2):
            self.down1 = nn.MaxPool2d(kernel_size = 2)
            self.down2 = nn.MaxPool2d(kernel_size = 2)
            self.down3 = nn.MaxPool2d(kernel_size = 2)
        else:
            self.down1 = nn.MaxPool3d(kernel_size = 2)
            self.down2 = nn.MaxPool3d(kernel_size = 2)
            self.down3 = nn.MaxPool3d(kernel_size = 2)           

        DeconvLayer = self.get_deconv_layer(self.depth_sep_deconv)
        if(self.resolution_level == 5):
            if(self.dimension == 2):
                self.down4 = nn.MaxPool2d(kernel_size = 2)
            else:
                self.down4 = nn.MaxPool3d(kernel_size = 2)
            self.up1 = DeconvLayer(self.ft_chns[4], self.ft_chns[3], kernel_size = 2,
                dim = self.dimension, stride = 2, groups = 1, acti_func = get_acti_func(self.acti_func, self.params))
        self.up2 = DeconvLayer(self.ft_chns[3], self.ft_chns[2], kernel_size = 2,
                dim = self.dimension, stride = 2, groups = 1, acti_func = get_acti_func(self.acti_func, self.params))
        self.up3 = DeconvLayer(self.ft_chns[2], self.ft_chns[1], kernel_size = 2,
                dim = self.dimension, stride = 2, groups = 1, acti_func = get_acti_func(self.acti_func, self.params))
        self.up4 = DeconvLayer(self.ft_chns[1], self.ft_chns[0], kernel_size = 2,
                dim = self.dimension, stride = 2, groups = 1, acti_func = get_acti_func(self.acti_func, self.params))

        if(self.dropout):
            self.drop1 = nn.Dropout(p=0.1)
            self.drop2 = nn.Dropout(p=0.2)
            self.drop3 = nn.Dropout(p=0.3)
            self.drop4 = nn.Dropout(p=0.4)
            if(self.resolution_level == 5):
                self.drop5 = nn.Dropout(p=0.5)
        
        if(self.deep_spv):
            if(self.dimension == 2):
                self.conv7 = nn.Conv2d(self.ft_chns[2], self.n_class,
                    kernel_size = 3, padding = 1)
                self.conv8 = nn.Conv2d(self.ft_chns[1], self.n_class,
                    kernel_size = 3, padding = 1)
            else:
                self.conv7 = nn.Conv3d(self.ft_chns[2], self.n_class,
                    kernel_size = 3, padding = 1)
                self.conv8 = nn.Conv3d(self.ft_chns[1], self.n_class,
                    kernel_size = 3, padding = 1)

        if(self.dimension == 2):
            self.conv9 = nn.Conv2d(self.ft_chns[0], self.n_class, 
                kernel_size = 3, padding = 1)
        else:
            self.conv9 = nn.Conv3d(self.ft_chns[0], self.n_class, 
                kernel_size = 3, padding = 1)

    def forward(self, x):
        x_shape = list(x.shape)
        if(len(x_shape)==5 and self.dimension == 2):
            [N, C, D, H, W] = x_shape
            new_shape = [N*D, C, H, W]
            x = torch.transpose(x, 1, 2)
            x = torch.reshape(x, new_shape)
        f1 = self.block1(x)
        if(self.pe_block):
            f1 = self.pe1(f1)
        if(self.dropout):
             f1 = self.drop1(f1)
        d1 = self.down1(f1)

        f2 = self.block2(d1)
        if(self.pe_block):
            f2 = self.pe2(f2)
        if(self.dropout):
             f2 = self.drop2(f2)
        d2 = self.down2(f2)

        f3 = self.block3(d2)
        if(self.pe_block):
            f3 = self.pe3(f3)
        if(self.dropout):
             f3 = self.drop3(f3)
        d3 = self.down3(f3)

        f4 = self.block4(d3)
        if(self.pe_block):
            f4 = self.pe4(f4)
        if(self.dropout):
             f4 = self.drop4(f4)

        if(self.resolution_level == 5):
            d4 = self.down4(f4)
            f5 = self.block5(d4)
            if(self.pe_block):
                f5 = self.pe5(f5)
            if(self.dropout):
                f5 = self.drop5(f5)

            f5up  = self.up1(f5)
            f4cat = torch.cat((f4, f5up), dim = 1)
            f6    = self.block6(f4cat)
            if(self.pe_block):
                f6 = self.pe6(f6)
            f6up  = self.up2(f6)
            f3cat = torch.cat((f3, f6up), dim = 1)
        else:
            f4up  = self.up2(f4)
            f3cat = torch.cat((f3, f4up), dim = 1)
        f7    = self.block7(f3cat)
        if(self.pe_block):
            f7 = self.pe7(f7)
        f7up  = self.up3(f7)
        if(self.deep_spv):
            interp_mode = 'bilinear' if self.dimension == 2 else 'trilinear'
            f7pred = self.conv7(f7)
            f7predup_out = nn.functional.interpolate(f7pred,
                        size = list(x.shape)[2:], mode = interp_mode)

        f2cat = torch.cat((f2, f7up), dim = 1)
        f8    = self.block8(f2cat)
        if(self.pe_block):
            f8 = self.pe8(f8)
        f8up  = self.up4(f8)
        if(self.deep_spv):
            f8pred = self.conv8(f8)
            f8predup_out = nn.functional.interpolate(f8pred,
                        size = list(x.shape)[2:], mode = interp_mode)

        f1cat = torch.cat((f1, f8up), dim = 1)
        f9    = self.block9(f1cat)
        if(self.pe_block):
            f9 = self.pe9(f9)
        output = self.conv9(f9)

        if(len(x_shape)==5 and self.dimension == 2):
            new_shape = [N, D] + list(output.shape)[1:]
            output = torch.reshape(output, new_shape)
            output = torch.transpose(output, 1, 2)

            if(self.deep_spv):
                f7predup_out = torch.reshape(f7predup_out, new_shape)
                f7predup_out = torch.transpose(f7predup_out, 1, 2)
                f8predup_out = torch.reshape(f8predup_out, new_shape)
                f8predup_out = torch.transpose(f8predup_out, 1, 2)
        if(self.deep_spv):
            return output, f7predup_out, f8predup_out
        else:
            return output

