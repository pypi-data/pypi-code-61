# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 10:45:43 2016

@author: nick

"""
from netCDF4 import Dataset
import numpy as np
import os
import glob
from dateutil.parser import parse 
from datetime import datetime


def read_scc(dir_inp, station, end_fill):
        
    lidar_path_all = []

    lidar_path_all = glob.glob(dir_inp + '*_'+station+'*.nc')

    date_m = np.empty((len(lidar_path_all),),dtype='object')
    for i in range(0,len(lidar_path_all)):
        bname = os.path.basename(lidar_path_all[i])
        date_m[i] = os.path.splitext(bname)[0][bname.find('_')+4:bname.find('.')]
    
    date_u = np.sort(list(set(date_m)))

    prod_arr = []
    alt_arr = []
    label_w_arr = []
    dt_start_arr = []
    fname = []
    metadata = []
    true_lims = []
    for k in range(len(date_u)):
        # Use only backscatter profiles
        lidar_path_u = glob.glob(dir_inp + '/*_*'+date_u[k]+'.b*.nc') 
        if lidar_path_u:            
            arg = []
            for path in lidar_path_u:
                arg.append(os.path.splitext(os.path.splitext(os.path.basename(path))[0])[1][0:3])
                fh = Dataset(path, mode='r')
                temp_meta = fh.__dict__
                temp_meta['title'] = 'Geometrical properties of aerosol layers'
                
                # Dates
                start_m = parse(fh.measurement_start_datetime)
                dt_start = datetime(start_m.year, start_m.month, start_m.day, 
                                    start_m.hour, start_m.minute, start_m.second)
                
                # Profiles
                alt = np.round(fh.variables['altitude'][:].data/1000., decimals = 5)
                prod = 1e6*fh.variables['backscatter'][0, 0, :].data
                rh = (fh.variables['backscatter_calibration_range'][0,1] + fh.variables['backscatter_calibration_range'][0,0])/2.
                
                # Nans above the reference height and where prod =  9.96920997e+36              
                step = np.round(alt[1] - alt[0], decimals = 5)
                mask = (alt < rh) & (prod >= 0.) & (prod < 1e6)
                
                prod = prod[mask]
                alt = alt[mask]                
                
                if (len(alt) > 0) & (len(prod) > 0):
                    # Interpolate intermediate nans and also keep nan above half wavelet step above end
                    alt_n = np.round(np.arange(alt[0] - end_fill, alt[-1] + end_fill, step), decimals = 5)
                    prod_n = np.interp(alt_n, np.hstack((alt[0] - end_fill, alt, alt[-1] + end_fill)),
                                       np.hstack((prod[0], prod, prod[-1])))
                    label_w = arg[0][1:2] + str(int(fh.variables['wavelength'][0]))
                    
                    print('File - ' + date_u[k] + ' - ' + label_w)
                    
                    # Append to lists
                    if (len(prod[prod == prod]) > 10) & (len(alt[prod > 0.]) > 10):
                        dt_start_arr.append(dt_start)
                        alt_arr.append(alt_n)
                        prod_arr.append(prod_n)
                        label_w_arr.append(label_w)
                        fname.append(os.path.splitext(os.path.splitext(os.path.basename(path))[0])[0])
                        temp_meta['input_file'] = fname[-1]
                        metadata.append(temp_meta)
                        true_lims.append([alt[0], alt[-1]])

    return(dt_start_arr, alt_arr, prod_arr, label_w_arr, metadata)