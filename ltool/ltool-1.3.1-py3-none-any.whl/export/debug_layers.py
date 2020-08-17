#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 22:36:59 2019

@author: nick
"""

from matplotlib import pyplot as plt
import os

def debug_layers(date, wave, alt, wct, sig, geom, thres, dir_out):
        
    if not os.path.exists(dir_out + '/debug/'):
        os.makedirs(dir_out + '/debug/')
    
    # sig_ulim = pd.Series([10.,5.,1.], ['355', '532', '1064'])

    bases = geom.sel(features = 'base').values
    tops = geom.sel(features = 'top').values
    coms = geom.sel(features = 'center_of_mass').values
    peaks = geom.sel(features = 'peak').values
    
    # Plots
    plt.figure
    plt.subplot(121)
    xlims = [-10., 10.]
    ylims = [0, 10.]
    plt.title('Normalized WCT')
    plt.plot([-0.25, -0.25], ylims, '--', color = 'lightgreen')
    plt.plot([0.25, 0.25], ylims, '--', color = 'darkgreen')
    for i in range(geom.shape[0]):
        if geom.sel(features='residual_layer_flag').values[i] == 1:
            clrs = ['gray', 'black', 'grey']
        if geom.sel(features='residual_layer_flag').values[i] == 0:
            clrs = ['purple', 'cyan', 'purple']
        plt.plot(xlims, [bases[i], bases[i]], color = clrs[0])
        plt.plot(xlims, [tops[i], tops[i]], color = clrs[1])
        plt.axhspan(bases[i], tops[i], facecolor = clrs[2], alpha = 0.2)
    plt.plot(wct, alt)
    plt.axis(xlims + ylims)
    plt.xlabel('WCT')
    plt.ylabel('Altitude [m]')
    
    plt.subplot(122)
    xlims = [-thres, 20.*thres]
    ylims = [0, 10.]
    plt.title('Product')
    plt.plot([thres, thres], ylims, '--', color = 'black', alpha = 0.5)
    for i in range(geom.shape[0]):
        if geom.sel(features='residual_layer_flag').values[i] == 1:
            clrs = ['gray', 'black', 'grey']
        if geom.sel(features='residual_layer_flag').values[i] == 0:
            clrs = ['purple', 'cyan', 'purple']
        plt.plot(xlims, [bases[i], bases[i]], color = clrs[0])
        plt.plot(xlims, [tops[i], tops[i]], color =  clrs[1])
        plt.plot(xlims, [coms[i], coms[i]], '--', color = 'goldenrod')
        plt.scatter(sig[alt == peaks[i]], peaks[i], 
                    marker = '*', s = 250, color = 'goldenrod')
        plt.axhspan(bases[i], tops[i], facecolor = 'purple', alpha = 0.2)
    plt.plot(sig, alt)
    plt.axis(xlims + ylims)
    plt.xlabel('Backscatter at '+ wave[1:] +'nm [$Mm^{-1} \cdot sr^{-1}$]')
    plt.ylabel('Altitude [m]')
    
    plt.tight_layout()
    plt.savefig(dir_out + '/debug/' + date.strftime('%Y%m%d_%H%M%S') + '_' + wave + '.png')
    plt.close()
    
    return()
