# -*- coding: utf-8 -*-
from __future__ import print_function, division

import torch
import torch.nn as nn
import numpy as np


def vnet_dice_loss(predict, soft_y, softmax = True):
    if(softmax):
        predict = nn.Softmax(dim = 1)(predict)
    predict = reshape_tensor_to_2D(predict)
    soft_y  = reshape_tensor_to_2D(soft_y) 
    y_vol = torch.sum(soft_y*soft_y,   dim = 0)
    p_vol = torch.sum(predict*predict, dim = 0)
    intersect = torch.sum(soft_y * predict, dim = 0)
    dice_score = (2.0 * intersect + 1e-5)/ (y_vol + p_vol + 1e-5)
    dice_loss  = 1.0 - torch.mean(dice_score)
    return dice_loss

def mae_loss(predict, soft_y, softmax = True):
    """
    loss based on mean absolute value of error. 
    """
    if(softmax):
        predict = nn.Softmax(dim = 1)(predict)
    diff = predict - soft_y
    mae  = diff.abs().mean()
    return mae

def mse_loss(predict, soft_y, softmax = True):
    """
    loss based on mean absolute value of error. 
    """
    if(softmax):
        predict = nn.Softmax(dim = 1)(predict)
    diff = predict - soft_y
    mse  = diff*diff 
    mse  = mse.mean()
    return mse

def exp_log_loss(predict, soft_y, softmax = True):
    """
    The exponential logarithmic loss in this paper: 
    Ken C. L. Wong, Mehdi Moradi, Hui Tang, Tanveer F. Syeda-Mahmood: 3D Segmentation with 
    Exponential Logarithmic Loss for Highly Unbalanced Object Sizes. MICCAI (3) 2018: 612-619.
    """
    if(softmax):
        predict = nn.Softmax(dim = 1)(predict)
    predict = reshape_tensor_to_2D(predict)
    soft_y  = reshape_tensor_to_2D(soft_y)
    gamma   = 0.3
    w_dice  = 0.8
    dice_score = get_classwise_dice(predict, soft_y)
    dice_score = 0.01 + dice_score * 0.98
    exp_dice   = -torch.log(dice_score)
    exp_dice   = torch.pow(exp_dice, gamma)
    exp_dice   = torch.mean(exp_dice)

    predict= 0.01 + predict * 0.98
    wc     = torch.mean(soft_y, dim = 0)
    wc     = 1.0 / (wc + 0.1)
    wc     = torch.pow(wc, 0.5)
    ce     = - torch.log(predict)
    exp_ce = wc * torch.pow(ce, gamma)
    exp_ce = torch.sum(soft_y * exp_ce, dim = 1)
    exp_ce = torch.mean(exp_ce)

    loss = exp_dice * w_dice + exp_ce * (1.0 - w_dice)
    return loss


def volume_weighted_dice(predict, soft_y, softmax = True):
    if(softmax):
        predict = nn.Softmax(dim = 1)(predict)
    predict = reshape_tensor_to_2D(predict)
    soft_y  = reshape_tensor_to_2D(soft_y)
    dice_score = get_classwise_dice(predict, soft_y)
    vol = torch.sum(soft_y, dim = 0)
    wht = 1.0 - nn.Softmax()(vol)
    dice_loss  = 1.0 - torch.sum(dice_score * wht)   
    return dice_loss

def ce_dice_loss(predict, soft_y, softmax = True):
    if(softmax):
        predict = nn.Softmax(dim = 1)(predict)
    predict = reshape_tensor_to_2D(predict)
    soft_y  = reshape_tensor_to_2D(soft_y) 

    predict = predict * 0.98 + 0.01
    ce = - soft_y * torch.log(predict)
    ce = torch.sum(ce, dim = 1)
    ce = torch.mean(ce)

    dice_score = get_classwise_dice(predict, soft_y)
    dice_loss  = 1.0 - torch.mean(dice_score)

    loss = ce + dice_loss
    return loss

def mae_dice_loss(predict, soft_y, softmax = True):
    if(softmax):
        predict = nn.Softmax(dim = 1)(predict)
    predict = reshape_tensor_to_2D(predict)
    soft_y  = reshape_tensor_to_2D(soft_y) 

    diff = predict - soft_y
    mae  = diff.abs().mean()

    dice_score = get_classwise_dice(predict, soft_y)
    dice_loss  = 1.0 - torch.mean(dice_score)

    loss = mae + dice_loss
    return loss

def focal_dice_loss(predict, soft_y, softmax = True):
    """
    focal dice according to the following paper:
        Pei Wang, Albert C. S. Chung: Focal Dice Loss and Image Dilation for Brain Tumor Segmentation. 
        DLMIA/ML-CDS@MICCAI 2018: 119-127
    """
    if(softmax):
        predict = nn.Softmax(dim = 1)(predict)
    predict = reshape_tensor_to_2D(predict)
    soft_y  = reshape_tensor_to_2D(soft_y) 

    beta  = 0.5   # beta < 1.0 to down-weight hard class
    dice_score = get_classwise_dice(predict, soft_y)
    dice_score = 0.01 + dice_score * 0.98
    dice_score = torch.pow(dice_score, 1.0/beta)
    dice_loss  = 1.0 - torch.mean(dice_score)
    return dice_loss

def uncertainty_dice_loss(predict, soft_y, gumb, softmax = True):
    predict_g = predict + gumb
    predict_g = nn.Softmax(dim = 1)(predict_g)
    predict_g, soft_y = reshape_prediction_and_ground_truth(predict_g, soft_y) 
    dice_score = get_classwise_dice(predict_g, soft_y)
    dice_loss  = 1.0 - torch.mean(dice_score)  
    return dice_loss

def volume_dice_loss(predict, soft_y, softmax = True):
    if(softmax):
        predict = nn.Softmax(dim = 1)(predict)
    predict, soft_y = reshape_prediction_and_ground_truth(predict, soft_y)
    dice_score = get_classwise_dice(predict, soft_y)
    dice_loss  = 1.0 - torch.mean(dice_score)

    vp = torch.sum(predict, dim = 0)
    vy = torch.sum(predict, dim = 0)
    v_loss = (vp - vy)/vy
    v_loss = v_loss * v_loss
    v_loss = torch.mean(v_loss)

    loss = dice_loss + v_loss * 0.2
    return loss


def hardness_weight_dice_loss(predict, soft_y, softmax = True):
    """
    voxel-wise hardness weighted dice loss, proposed in the following paper:
    Guotai Wang, Jonathan Shapey, Wenqi Li, et al. Automatic Segmentation of Vestibular Schwannoma from 
    T2-Weighted MRI by Deep Spatial Attention with Hardness-Weighted Loss. MICCAI (2) 2019: 264-272
    """
    if(softmax):
        predict = nn.Softmax(dim = 1)(predict)
    predict = reshape_tensor_to_2D(predict)
    soft_y  = reshape_tensor_to_2D(soft_y) 

    weight = torch.abs(predict - soft_y)
    lamb   = 0.6
    weight = lamb + weight*(1 - lamb)

    y_vol = torch.sum(soft_y*weight,  dim = 0)
    p_vol = torch.sum(predict*weight, dim = 0)
    intersect = torch.sum(soft_y * predict * weight, dim = 0)
    dice_score = (2.0 * intersect + 1e-5)/ (y_vol + p_vol + 1e-5)
    dice_loss  = 1.0 - torch.mean(dice_score)   
    return dice_loss

def exponentialized_dice_loss(predict, soft_y, softmax = True):
    if(softmax):
        predict = nn.Softmax(dim = 1)(predict)
    predict = reshape_tensor_to_2D(predict)
    soft_y  = reshape_tensor_to_2D(soft_y)  
    dice_score = get_classwise_dice(predict, soft_y)
    exp_dice = - torch.log(dice_score)
    exp_dice = torch.mean(exp_dice)
    return exp_dice

def generalized_dice_loss(predict, soft_y, softmax = True):
    tensor_dim = len(predict.size())
    num_class  = list(predict.size())[1]
    if(softmax):
        predict = nn.Softmax(dim = 1)(predict)
    if(tensor_dim == 5):
        soft_y  = soft_y.permute(0, 2, 3, 4, 1)
        predict = predict.permute(0, 2, 3, 4, 1)
    elif(tensor_dim == 4):
        soft_y  = soft_y.permute(0, 2, 3, 1)
        predict = predict.permute(0, 2, 3, 1)
    else:
        raise ValueError("{0:}D tensor not supported".format(tensor_dim))
    
    soft_y  = torch.reshape(soft_y,  (-1, num_class))
    predict = torch.reshape(predict, (-1, num_class))
    num_voxel = list(soft_y.size())[0]
    vol = torch.sum(soft_y, dim = 0)
    weight = (num_voxel - vol)/num_voxel
    intersect = torch.sum(predict * soft_y, dim = 0)
    intersect = torch.sum(weight * intersect)
    vol_sum = torch.sum(soft_y, dim = 0) + torch.sum(predict, dim = 0)
    vol_sum = torch.sum(weight * vol_sum)
    dice_score = (2.0 * intersect + 1e-5) / (vol_sum + 1e-5)
    dice_loss = 1.0 - dice_score
    return dice_loss

def distance_loss(predict, soft_y, lab_distance, softmax = True):
    """
    get distance loss function
    lab_distance is unsigned distance transform of foreground contour
    """
    tensor_dim = len(predict.size())
    num_class  = list(predict.size())[1]
    if(softmax):
        predict = nn.Softmax(dim = 1)(predict)
    if(tensor_dim == 5):
        lab_distance  = lab_distance.permute(0, 2, 3, 4, 1)
        predict = predict.permute(0, 2, 3, 4, 1)
        soft_y  = soft_y.permute(0, 2, 3, 4, 1)
    elif(tensor_dim == 4):
        lab_distance  = lab_distance.permute(0, 2, 3, 1)
        predict = predict.permute(0, 2, 3, 1)
        soft_y  = soft_y.permute(0, 2, 3, 1)
    else:
        raise ValueError("{0:}D tensor not supported".format(tensor_dim))

    lab_distance  = torch.reshape(lab_distance,  (-1, num_class))
    predict = torch.reshape(predict, (-1, num_class))
    soft_y  = torch.reshape(soft_y, (-1, num_class))

    # mis_seg  = torch.abs(predict - soft_y)
    dis_sum  = torch.sum(lab_distance * predict, dim = 0)
    vox_sum  = torch.sum(predict, dim = 0)
    avg_dis  = (dis_sum + 1e-5)/(vox_sum + 1e-5)
    avg_dis  = torch.mean(avg_dis)
    return avg_dis  


