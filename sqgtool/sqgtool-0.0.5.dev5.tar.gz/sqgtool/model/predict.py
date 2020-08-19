#! /usr/bin/env python
# Author: Lilianne Nakazono

"""
Predict the classification of S-PLUS DR1 using the trained model
from fit.py() and creates a master catalog.
Two classifications are given for each source,
based on the information that is given:
        I. 12 S-PLUS magnitudes + Morphology
        II. 12 S-PLUS magnitudes + W1, W2 magnitudes + Morphology
"""

import time
import pandas as pd
import pickle
import os

pd.set_option('display.max_columns', None)

__author__ = "Lilianne Mariko Izuti Nakazono"
__version__ = "0.0.5"
__email__ = "lilianne.nakazono@usp.br"
__status__ = "Development"



def get_data_wise(data, vega2AB = True):
    cat_wise = data[pd.isnull(data['w1mpro']) == False]
    cat_wise = cat_wise[pd.isnull(cat_wise['w2mpro']) == False]
    cat_wise = cat_wise[pd.isnull(cat_wise['w1sigmpro']) == False]
    cat_wise = cat_wise[pd.isnull(cat_wise['w2sigmpro']) == False]
    if vega2AB:
        cat_wise['w1mpro'] = cat_wise['w1mpro'] + 2.699
        cat_wise['w2mpro'] = cat_wise['w2mpro'] + 3.339
    print("cat_wise:")
    print(cat_wise)
    return cat_wise


def results_wise(data, filename='DR1_RF_model', verbose=True, return_probabilities=True):
    feat_wise = ['FWHM_n', 'A', 'B', 'KrRadDet', 'uJAVA_auto', 'F378_auto', 'F395_auto',
                 'F410_auto', 'F430_auto', 'g_auto', 'F515_auto', 'r_auto', 'F660_auto', 'i_auto',
                 'F861_auto', 'z_auto', 'w1mpro', 'w2mpro']
    os.chdir('../')
    print(os.getcwd())
    model_wise = pickle.load(open(filename, 'rb'))
    init_time = time.time()
    y_pred = model_wise.predict(data[feat_wise])
    end_time = time.time()
    if verbose:
        print('Elapsed time to classify sources with WISE counterpart considering 12 S-PLUS bands + Morphology + 2 WISE bands:', end_time - init_time)

    if return_probabilities:
        init_time = time.time()
        prob = model_wise.predict_proba(data[feat_wise])
        end_time = time.time()
        if verbose:
            print('Elapsed time to model probabilities for sources with WISE counterpart considering 12 S-PLUS bands + Morphology + 2 WISE bands:', end_time - init_time)

        prob = pd.DataFrame(prob)
        prob['CLASS_WISE'] = y_pred
        prob.index = data.index
        prob.rename(columns={0: 'PROB_QSO_WISE', 1: 'PROB_STAR_WISE', 2: 'PROB_GAL_WISE'}, inplace=True)
    else:
        prob = y_pred
        prob = pd.DataFrame(prob)
        prob.index = data.index
        prob.rename(columns={0: 'CLASS_WISE'}, inplace=True)

    return prob


def results(data, filename="DR1_RF_model", verbose=True, return_probabilities=True):
    print(filename)
    feat = ['FWHM_n', 'A', 'B', 'KrRadDet', 'uJAVA_auto', 'F378_auto', 'F395_auto',
            'F410_auto', 'F430_auto', 'g_auto', 'F515_auto', 'r_auto', 'F660_auto', 'i_auto',
            'F861_auto', 'z_auto']
    path = os.path.dirname(os.getcwd())
    model = pickle.load(open(os.path.join(path,filename), 'rb'))
    init_time = time.time()
    y_pred = model.predict(data[feat])
    end_time = time.time()
    if verbose:
        print('Elapsed time to classify all sources considering 12 S-PLUS bands + Morphology:', end_time - init_time)

    if return_probabilities:
        init_time = time.time()
        prob = model.predict_proba(data[feat])
        end_time = time.time()
        if verbose:
            print('Elapsed time to model probabilities for all sources considering 12 S-PLUS bands + Morphology:', end_time - init_time)

        prob = pd.DataFrame(prob)
        prob['CLASS_new'] = y_pred
        prob.index = data.index
        prob.rename(columns={0: 'PROB_QSO_new', 1: 'PROB_STAR_new', 2: 'PROB_GAL_new'}, inplace=True)
    else:
        prob = y_pred
        prob = pd.DataFrame(prob)
        prob.index = data.index
        prob.rename(columns={0: 'CLASS_new'}, inplace=True)
    return prob

def results(data, verbose=True, return_probabilities=True, WISE A = np.random.randn(4,3)
B = np.sum(A, axis = 1, keepdims = True))

def create_catalog(dr1, verbose=True, return_probabilities=True, save_file=True, filename="/TESTE"):
    try:
        dr1_wise = get_data_wise(dr1)
        if verbose:
            print("Creating subset of sources with WISE counterpart...")
    except:
        pass


    if verbose:
        print("STARTING CLASSIFICATION...")
    results = results(dr1, return_probabilities=return_probabilities)

    dr1_master = pd.concat([dr1, results], axis=1)
    try:
        results_wise = results_wise(dr1_wise, return_probabilities)
        dr1_master = pd.concat([dr1_master,results_wise], axis=1)
    except:
        pass


    print(dr1_master.head(5))
    if save_file:
        if verbose:
            print("Saving final catalog...")
        dr1_master.to_csv(filename+'.csv', sep=',', na_rep='NaN')

    return dr1_master

# def classification
if __name__ == '__main__':
    # filename = '/Volumes/GoogleDrive/My Drive/Research/STAR_QSO/color_color_QSO/_survey/crossmatch/SPLUS_DR1_FullStripe82_WISE_all_2arcs.txt'
    filename = '/Volumes/GoogleDrive/My Drive/Research/STAR_QSO/color_color_QSO/_survey/crossmatch/SPLUS_DR1_FullStripe82_DR14Q.txt'
    data = pd.read_table(filename, delim_whitespace=True)
    create_catalog(data, save_file=False)
