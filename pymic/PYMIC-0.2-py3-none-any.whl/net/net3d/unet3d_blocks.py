# -*- coding: utf-8 -*-
from __future__ import print_function, division

import time
import torch
import torch.nn as nn
import numpy as np
from pymic.layer.activation import get_acti_func
from pymic.layer.convolution import ConvolutionLayer, DepthSeperableConvolutionLayer
from pymic.layer.deconvolution import DeconvolutionLayer, DepthSeperableDeconvolutionLayer

class UNetBlock_SpatialSep(nn.Module):
    def __init__(self, dim, in_channels, out_channels, norm_type, groups, acti_func, acti_func_param):
        super(UNetBlock_SpatialSep, self).__init__()
        assert(dim == 3)
        self.dim       = dim
        self.in_chns   = in_channels
        self.out_chns  = out_channels
        self.acti_func = acti_func

        self.conv1_a = ConvolutionLayer(in_channels,  out_channels, (1, 3, 3), 
                dim = self.dim, padding = (0, 1, 1), conv_group = groups, norm_type = norm_type, norm_group = groups,
                acti_func=get_acti_func(acti_func, acti_func_param))
        self.conv1_b = ConvolutionLayer(out_channels,  out_channels, (3, 1, 1), 
                dim = self.dim, padding = (1, 0, 0), conv_group = groups, norm_type = norm_type, norm_group = groups,
                acti_func=get_acti_func(acti_func, acti_func_param))        
        self.conv2_a = ConvolutionLayer(out_channels, out_channels, (1, 3, 3), 
                dim = self.dim, padding = (0, 1, 1), conv_group = groups, norm_type = norm_type, norm_group = groups,
                acti_func=get_acti_func(acti_func, acti_func_param))
        self.conv2_b = ConvolutionLayer(out_channels, out_channels, (3, 1, 1), 
                dim = self.dim, padding = (1, 0, 0), conv_group = groups, norm_type = norm_type, norm_group = groups,
                acti_func=get_acti_func(acti_func, acti_func_param))


    def forward(self, x):
        f1 = self.conv1_a(x)
        f1 = self.conv1_b(f1)
        f2 = self.conv2_a(f1)
        f2 = self.conv2_b(f2)
        return f2
        
class SpatialDepthSeperableConvolutionLayer(nn.Module):
    """
    A compose layer with the following components:
    convolution -> (batch_norm) -> activation -> (dropout)
    batch norm and dropout are optional
    """
    def __init__(self, in_channels, out_channels, dim = 3,
            conv_group = 1, bias = True, 
            norm_type = 'batch_norm', norm_group = 1, acti_func = None):
        super(SpatialDepthSeperableConvolutionLayer, self).__init__()
        assert(dim == 3)
        self.n_in_chns  = in_channels
        self.n_out_chns = out_channels
        self.norm_type  = norm_type
        self.norm_group = norm_group
        self.acti_func  = acti_func

        stride   = (1, 1, 1)
        dilation = (1, 1, 1)
        self.conv1x1 = nn.Conv3d(in_channels, out_channels,
            kernel_size = 1, stride = stride, padding = 0, dilation = dilation, groups = conv_group, bias = bias)   
        self.conv_inplane  = nn.Conv3d(out_channels, out_channels,
            (1, 3, 3), stride, (0, 1, 1), dilation, groups = out_channels, bias = bias)
        self.conv_outplane = nn.Conv3d(out_channels, out_channels,
            (3, 1, 1), stride, (1, 0, 0), dilation, groups = out_channels, bias = bias)
        if(self.norm_type == 'batch_norm'):
            self.bn = nn.modules.BatchNorm3d(out_channels)
        elif(self.norm_type == 'group_norm'):
            self.bn = nn.GroupNorm(self.norm_group, out_channels)
        elif(self.norm_type is not None):
            raise ValueError("unsupported normalization method {0:}".format(norm_type))

    def forward(self, x):
        f = self.conv1x1(x)
        f = self.conv_inplane(f)
        f = self.conv_outplane(f)
        if(self.norm_type is not None):
            f = self.bn(f)
        if(self.acti_func is not None):
            f = self.acti_func(f)
        return f

class UNetBlock_SpatialDepthSep(nn.Module):
    def __init__(self, dim, in_channels, out_channels, norm_type, groups, acti_func, acti_func_param):
        super(UNetBlock_SpatialDepthSep, self).__init__()
        assert(dim == 3)
        self.dim       = dim
        self.in_chns   = in_channels
        self.out_chns  = out_channels
        self.acti_func = acti_func

        self.conv1 = SpatialDepthSeperableConvolutionLayer(in_channels,  out_channels, 3, 
            conv_group = groups, norm_type = norm_type, norm_group = groups,
            acti_func=get_acti_func(acti_func, acti_func_param))
        self.conv2 = SpatialDepthSeperableConvolutionLayer(out_channels,  out_channels, 3, 
            conv_group = groups, norm_type = norm_type, norm_group = groups,
            acti_func=get_acti_func(acti_func, acti_func_param))

    def forward(self, x):
        f1 = self.conv1(x)
        f2 = self.conv2(f1)
        return f2

class SpatialDepthSeperableConvolutionLayer2(nn.Module):
    """
    A compose layer with the following components:
    convolution -> (batch_norm) -> activation -> (dropout)
    batch norm and dropout are optional
    """
    def __init__(self, in_channels, out_channels, dim = 3,
            conv_group = 1, bias = True, 
            norm_type = 'batch_norm', norm_group = 1, acti_func = None):
        super(SpatialDepthSeperableConvolutionLayer2, self).__init__()
        assert(dim == 3)
        self.n_in_chns  = in_channels
        self.n_out_chns = out_channels
        self.norm_type  = norm_type
        self.norm_group = norm_group
        self.acti_func  = acti_func

        stride   = (1, 1, 1)
        dilation = (1, 1, 1)
        self.conv1x1 = nn.Conv3d(in_channels, out_channels,
            kernel_size = 1, stride = stride, padding = 0, dilation = dilation, groups = conv_group, bias = bias)   
        self.conv_inplane  = nn.Conv3d(out_channels, out_channels,
            (1, 3, 3), stride, (0, 1, 1), dilation, groups = out_channels, bias = bias)
        self.conv_outplane = nn.Conv3d(out_channels, out_channels,
            (3, 1, 1), stride, (1, 0, 0), dilation, groups = out_channels, bias = bias)
        if(self.norm_type == 'batch_norm'):
            self.bn = nn.modules.BatchNorm3d(out_channels)
        elif(self.norm_type == 'group_norm'):
            self.bn = nn.GroupNorm(self.norm_group, out_channels)
        elif(self.norm_type is not None):
            raise ValueError("unsupported normalization method {0:}".format(norm_type))

    def forward(self, x):
        f1 = self.conv1x1(x)
        f2 = self.conv_inplane(f1)
        f3 = self.conv_outplane(f2)
        if(self.norm_type is not None):
            f3 = self.bn(f3)
        if(self.acti_func is not None):
            f3 = self.acti_func(f3)
        return f3

class UNetBlock_SpatialDepthSep2(nn.Module):
    def __init__(self, dim, in_channels, out_channels, norm_type, groups, acti_func, acti_func_param):
        super(UNetBlock_SpatialDepthSep2, self).__init__()
        assert(dim == 3)
        self.dim       = dim
        self.in_chns   = in_channels
        self.out_chns  = out_channels
        self.acti_func = acti_func

        self.conv1 = SpatialDepthSeperableConvolutionLayer2(in_channels,  out_channels, 3, 
            conv_group = groups, norm_type = norm_type, norm_group = groups,
            acti_func=get_acti_func(acti_func, acti_func_param))
        self.conv2 = SpatialDepthSeperableConvolutionLayer2(out_channels,  out_channels, 3, 
            conv_group = groups, norm_type = norm_type, norm_group = groups,
            acti_func=get_acti_func(acti_func, acti_func_param))

    def forward(self, x):
        f1 = self.conv1(x)
        f2 = self.conv2(f1)
        return f2