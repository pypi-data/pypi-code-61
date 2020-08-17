"""
Created on Sun May 17 21:06:52 2020

@author: nick
"""

import argparse
import os
import sys

def parse_config():
    parser = argparse.ArgumentParser(
    	description='Configuration file ')
    
    parser.add_argument('-m', '--measurement_id', metavar='m', 
                        type=str, nargs='+', 
                        help='The mesurement id that is going to be processed.')
    parser.add_argument('-c', '--config_file', metavar='c', 
                        type=str, nargs='+', 
                        help='Full path of the configuration file')
    
    args = parser.parse_args()
            
    meas_id = args.measurement_id[0]
    
    cfg_path = args.config_file[0]
        
    if not os.path.exists(cfg_path):
        print(f'-- Error: The configuration file was not found in the directory:{cfg_path} ')
        print('-- Program stopped')
        sys.exit(0)
    
    if len(args.config_file) > 1:
        print(f'-- Error: More than one configuration file paths provided ')
        print('-- Program stopped')
        sys.exit(0)

    if len(args.measurement_id) > 1:
        print(f'-- Error: More than one measurement IDs  provided ')
        print('-- Program stopped')
        sys.exit(0)
    
    return(meas_id, cfg_path)