#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 11:30:25 2019

@author: nick
"""
import pandas as pd

def st_info(st):
    
    earl_stations = pd.DataFrame(data=[[ 'Athens'                   ,   37.9600 ,   23.7800 ,  212. ],\
                                       [ 'Barcelona'                ,   41.3930 ,    2.1200 ,  115. ],\
                                       [ 'Belsk'                    ,   51.8300 ,   20.7800 ,  180. ],\
                                       [ 'Bucharest'                ,   44.3480 ,   26.0290 ,   93. ],\
                                       [ 'Cabauw'                   ,   51.9700 ,    4.9300 ,    0. ],\
                                       [ 'Clermont-Ferrant'         ,   45.7610 ,    3.1110 ,  420. ],\
                                       [ 'Evora'                    ,   38.5678 ,   -7.9115 ,  293. ],\
                                       [ 'Garmisch-Partenkirchen'   ,   47.4770 ,   11.0640 ,  730. ],\
                                       [ 'Granada'                  ,   37.1640 ,   -3.6050 ,  680. ],\
                                       [ 'Hamburg'                  ,   53.5680 ,    9.9730 ,   25. ],\
                                       [ 'Hauten-Provence'          ,   43.9000 ,    5.7000 ,  680. ],\
                                       [ 'Ispra'                    ,   45.8167 ,    8.6167 ,  209. ],\
                                       [ 'Jungfraujoch'             ,   46.5481 ,    7.9839 , 3580. ],\
                                       [ 'Kuehlungsborn'            ,   54.1200 ,   11.7700 ,   70. ],\
                                       [ 'Kuopio'                   ,   62.7333 ,   27.5500 ,  190. ],\
                                       [ 'LAquila'                  ,   42.3440 ,   13.3270 ,  683. ],\
                                       [ 'Lecce'                    ,   40.3330 ,   18.1000 ,   30. ],\
                                       [ 'Leipzig'                  ,   51.3500 ,   12.4330 ,   90. ],\
                                       [ 'Linkoping'                ,   58.3920 ,   15.5750 ,   70. ],\
                                       [ 'Madrid'                   ,   40.4565 ,   -3.7257 ,  669. ],\
                                       [ 'Maisach'                  ,   48.2090 ,   11.2580 ,  516. ],\
                                       [ 'Minsk'                    ,   53.9170 ,   27.6050 ,  200. ],\
                                       [ 'Naples'                   ,   40.8380 ,   14.1830 ,  118. ],\
                                       [ 'Neuchatel'                ,   47.0017 ,    6.9546 ,  478. ],\
                                       [ 'Palaisseau'               ,   48.7130 ,    2.2080 ,  156. ],\
                                       [ 'Potenza'                  ,   40.6000 ,   15.7200 ,  760. ],\
                                       [ 'Sofia'                    ,   42.6500 ,   23.3800 ,  550. ],\
                                       [ 'Thessaloniki'             ,   40.6300 ,   22.9500 ,   50. ],\
                                       [ 'Warsaw'                   ,   52.2100 ,   20.9800 ,  112. ]],\
    index=['at','ba','be','bu','ca','cl','evo','gp','gr','hh','hp','is',\
           'ju','kb','ku','la','lc','le','li','ma','ms','mi','na','ne',\
           'pl','pot','sf','the','wa'],columns=['Station','Latitude','Longtitude','Altitude'])
    
    station = earl_stations.loc[st, :]
    
    return(station)
