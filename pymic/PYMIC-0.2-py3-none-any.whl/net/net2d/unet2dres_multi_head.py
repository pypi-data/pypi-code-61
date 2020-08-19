import time
import torch
import torch.nn as nn
import numpy as np
from pymic.layer.activation import get_acti_func
from pymic.layer.convolution import ConvolutionLayer, DepthSeperableConvolutionLayer
from pymic.layer.deconvolution import DeconvolutionLayer, DepthSeperableDeconvolutionLayer
from pymic.net2d.unet2dres import get_acti_func, get_deconv_layer, get_unet_block, PEBlock

class UNet2DResMHead(nn.Module):
    def __init__(self, params):
        super(UNet2DResMHead, self).__init__()
        self.params = params
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

        Block = get_unet_block(self.block_type)
        self.block1 = Block(self.in_chns, self.ft_chns[0], self.norm_type, self.ft_groups[0],
             self.acti_func, self.params)

        self.block2 = Block(self.ft_chns[0], self.ft_chns[1], self.norm_type, self.ft_groups[1],
             self.acti_func, self.params)

        self.block3 = Block(self.ft_chns[1], self.ft_chns[2], self.norm_type, self.ft_groups[2],
             self.acti_func, self.params)

        self.block4 = Block(self.ft_chns[2], self.ft_chns[3], self.norm_type, self.ft_groups[3],
             self.acti_func, self.params)

        if(self.resolution_level == 5):
            self.block5 = Block(self.ft_chns[3], self.ft_chns[4], self.norm_type, self.ft_groups[4],
                self.acti_func, self.params)

            self.block6 = Block(self.ft_chns[3] * 2, self.ft_chns[3], self.norm_type, self.ft_groups[3],
                self.acti_func, self.params)

        self.block7 = Block(self.ft_chns[2] * 2, self.ft_chns[2], self.norm_type, self.ft_groups[2],
             self.acti_func, self.params)

        self.block8_1 = Block(self.ft_chns[1] * 2, self.ft_chns[1], self.norm_type, self.ft_groups[1],
             self.acti_func, self.params)
        
        self.block8_2 = Block(self.ft_chns[1] * 2, self.ft_chns[1], self.norm_type, self.ft_groups[1],
             self.acti_func, self.params)
        
        self.block8_3 = Block(self.ft_chns[1] * 2, self.ft_chns[1], self.norm_type, self.ft_groups[1],
             self.acti_func, self.params)

        self.block9_1 = Block(self.ft_chns[0] * 2, self.ft_chns[0], self.norm_type, self.ft_groups[0],
             self.acti_func, self.params)

        self.block9_2 = Block(self.ft_chns[0] * 2, self.ft_chns[0] - 8, self.norm_type, self.ft_groups[0],
             self.acti_func, self.params)
            
        self.block9_3 = Block(self.ft_chns[0] * 2, self.ft_chns[0] + 8, self.norm_type, self.ft_groups[0],
             self.acti_func, self.params)

        if(self.pe_block):
            self.pe1 = PEBlock(self.ft_chns[0], self.acti_func, self.params)
            self.pe2 = PEBlock(self.ft_chns[1], self.acti_func, self.params)
            self.pe3 = PEBlock(self.ft_chns[2], self.acti_func, self.params)
            self.pe4 = PEBlock(self.ft_chns[3], self.acti_func, self.params)
            self.pe7 = PEBlock(self.ft_chns[2], self.acti_func, self.params)
            self.pe8 = PEBlock(self.ft_chns[1], self.acti_func, self.params)
            self.pe9 = PEBlock(self.ft_chns[0], self.acti_func, self.params)
            if(self.resolution_level == 5):
                self.pe5 = PEBlock(self.ft_chns[4], self.acti_func, self.params)
                self.pe6 = PEBlock(self.ft_chns[3], self.acti_func, self.params)

        self.down1 = nn.MaxPool2d(kernel_size = 2)
        self.down2 = nn.MaxPool2d(kernel_size = 2)
        self.down3 = nn.MaxPool2d(kernel_size = 2)

        DeconvLayer = get_deconv_layer(self.depth_sep_deconv)
        if(self.resolution_level == 5):
            self.down4 = nn.MaxPool2d(kernel_size = 2)
            self.up1 = DeconvLayer(self.ft_chns[4], self.ft_chns[3], kernel_size = 2,
                dim = 2, stride = 2, groups = 1, acti_func = get_acti_func(self.acti_func, self.params))
        self.up2 = DeconvLayer(self.ft_chns[3], self.ft_chns[2], kernel_size = 2,
                dim = 2, stride = 2, groups = 1, acti_func = get_acti_func(self.acti_func, self.params))
        self.up3 = DeconvLayer(self.ft_chns[2], self.ft_chns[1], kernel_size = 2,
                dim = 2, stride = 2, groups = 1, acti_func = get_acti_func(self.acti_func, self.params))
        self.up4_1 = DeconvLayer(self.ft_chns[1], self.ft_chns[0], kernel_size = 2,
                dim = 2, stride = 2, groups = 1, acti_func = get_acti_func(self.acti_func, self.params))
        self.up4_2 = DeconvLayer(self.ft_chns[1], self.ft_chns[0], kernel_size = 2,
                dim = 2, stride = 2, groups = 1, acti_func = get_acti_func(self.acti_func, self.params))
        self.up4_3 = DeconvLayer(self.ft_chns[1], self.ft_chns[0], kernel_size = 2,
                dim = 2, stride = 2, groups = 1, acti_func = get_acti_func(self.acti_func, self.params))

        if(self.dropout):
            self.drop1 = nn.Dropout(p=0.1)
            self.drop2 = nn.Dropout(p=0.2)
            self.drop3 = nn.Dropout(p=0.3)
            self.drop4 = nn.Dropout(p=0.4)
            if(self.resolution_level == 5):
                self.drop5 = nn.Dropout(p=0.5)
            self.dropcat2_1 = nn.Dropout(p=0.3)
            self.dropcat2_2 = nn.Dropout(p=0.3)
            self.dropcat2_3 = nn.Dropout(p=0.3)

        
        if(self.deep_spv):
            self.conv7 = nn.Conv2d(self.ft_chns[2], self.n_class,
                kernel_size = 3, padding = 1)
            self.conv8 = nn.Conv2d(self.ft_chns[1], self.n_class,
                kernel_size = 3, padding = 1)

        self.conv9_1 = nn.Conv2d(self.ft_chns[0], self.n_class, 
            kernel_size = 3, padding = 1)
        
        self.conv9_2 = nn.Conv2d(self.ft_chns[0] - 8, self.n_class, 
            kernel_size = 3, padding = 1)
        
        self.conv9_3 = nn.Conv2d(self.ft_chns[0] + 8, self.n_class, 
            kernel_size = 3, padding = 1)
            

    def forward(self, x):
        x_shape = list(x.shape)
        if(len(x_shape)==5):
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
        # if(self.deep_spv):
        #     f7pred = self.conv7(f7)
        #     f7predup_out = nn.functional.interpolate(f7pred,
        #                 size = list(x.shape)[2:], mode = 'bilinear')

        f2cat = torch.cat((f2, f7up), dim = 1)
        if(self.dropout):
            f2cat_dr1 = self.dropcat2_1(f2cat)
            f2cat_dr2 = self.dropcat2_2(f2cat)
            f2cat_dr3 = self.dropcat2_3(f2cat)
            f8_1      = self.block8_1(f2cat_dr1)
            f8_2      = self.block8_2(f2cat_dr2)
            f8_3      = self.block8_3(f2cat_dr3)
        else:
            f8_1    = self.block8_1(f2cat)
            f8_2    = self.block8_2(f2cat)
            f8_3    = self.block8_3(f2cat)
        # if(self.pe_block):
        #     f8 = self.pe8(f8)
        f8up_1  = self.up4_1(f8_1)
        f8up_2  = self.up4_2(f8_2)
        f8up_3  = self.up4_3(f8_3)
        # if(self.deep_spv):
        #     f8pred = self.conv8(f8)
        #     f8predup_out = nn.functional.interpolate(f8pred,
        #                 size = list(x.shape)[2:], mode = 'bilinear')

        f1cat_1 = torch.cat((f1, f8up_1), dim = 1)
        f1cat_2 = torch.cat((f1, f8up_2), dim = 1)
        f1cat_3 = torch.cat((f1, f8up_3), dim = 1)
        f9_1    = self.block9_1(f1cat_1)
        f9_2    = self.block9_2(f1cat_2)
        f9_3    = self.block9_3(f1cat_3)
        # if(self.pe_block):
        #     f9 = self.pe9(f9)
        output1 = self.conv9_1(f9_1)
        output2 = self.conv9_2(f9_2)
        output3 = self.conv9_3(f9_3)

        if(len(x_shape)==5):
            new_shape = [N, D] + list(output1.shape)[1:]
            output1 = torch.reshape(output1, new_shape)
            output1 = torch.transpose(output1, 1, 2)
            output2 = torch.reshape(output2, new_shape)
            output2 = torch.transpose(output2, 1, 2)
            output3 = torch.reshape(output3, new_shape)
            output3 = torch.transpose(output3, 1, 2)

            # if(self.deep_spv):
            #     f7predup_out = torch.reshape(f7predup_out, new_shape)
            #     f7predup_out = torch.transpose(f7predup_out, 1, 2)
            #     f8predup_out = torch.reshape(f8predup_out, new_shape)
            #     f8predup_out = torch.transpose(f8predup_out, 1, 2)
        # if(self.deep_spv):
        #     return output, f8predup_out, f7predup_out
        # else:
        #     return output
        return output1, output2, output3
