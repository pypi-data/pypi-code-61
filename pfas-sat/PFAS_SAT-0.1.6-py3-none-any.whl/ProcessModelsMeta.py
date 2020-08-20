# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 20:48:42 2020

@author: msmsa
"""
ProcessModelsMeta = {}

ProcessModelsMeta['LandApp'] = {}
ProcessModelsMeta['LandApp']['Name'] = 'Land Application'
ProcessModelsMeta['LandApp']['File'] = 'LandApp.py'
ProcessModelsMeta['LandApp']['InputType'] = ['CompFin']

ProcessModelsMeta['Comp'] = {}
ProcessModelsMeta['Comp']['Name'] = 'Composting'
ProcessModelsMeta['Comp']['File'] = 'Comp.py'
ProcessModelsMeta['Comp']['InputType'] = ['CompFeed']

ProcessModelsMeta['Landfill'] = {}
ProcessModelsMeta['Landfill']['Name'] = 'Landfill'
ProcessModelsMeta['Landfill']['File'] = 'Landfill.py'
ProcessModelsMeta['Landfill']['InputType'] = ['MSW', 'CompFeed', 'CompFin']

ProcessModelsMeta['WWT'] = {}
ProcessModelsMeta['WWT']['Name'] = 'WWT'
ProcessModelsMeta['WWT']['File'] = 'WWT.py'
ProcessModelsMeta['WWT']['InputType'] = ['ContactWater', 'LF_Leachate']
