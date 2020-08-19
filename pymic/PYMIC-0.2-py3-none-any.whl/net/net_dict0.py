# -*- coding: utf-8 -*-
from __future__ import print_function, division
from pymic.net.net2d.unet2d import UNet2D
from pymic.net.net2d.cople_net import COPLENet
from pymic.net.net2d.unet2d_old import UNet2DOld
from pymic.net.net2d.unet2d_attention import AttentionUNet2D
from pymic.net.net2d.eespnet_v2 import EESPNetV2
from pymic.net.net2d.unet2d_scse import UNet2D_ScSE
from pymic.net.net2d.unet2d_covidv2 import UNet2D_COVIDV2
from pymic.net.net2d.unet2d_covidv2_variants import UNet2D_COVIDV3, UNet2D_COVIDV4, UNet2D_COVIDV5
from pymic.net.net3d.unet2d5 import UNet2D5
from pymic.net.net3d.unet3d import UNet3D

NetDict = {
	'UNet2D': UNet2D,
	'COPLENet': COPLENet,
	'UNet2DOld': UNet2DOld,
	'EESPNetV2':EESPNetV2,
	'AttentionUNet2D': AttentionUNet2D,
	'UNet2D_ScSE': UNet2D_ScSE,
    'UNet2D_COVIDV2':UNet2D_COVIDV2,
	'UNet2D_COVIDV3':UNet2D_COVIDV3,
	'UNet2D_COVIDV4':UNet2D_COVIDV4,
	'UNet2D_COVIDV5':UNet2D_COVIDV5,
	'UNet2D5': UNet2D5,
	'UNet3D': UNet3D
	}
