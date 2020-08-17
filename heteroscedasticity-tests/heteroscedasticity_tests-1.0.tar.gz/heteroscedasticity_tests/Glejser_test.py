# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 23:50:51 2020

@author: Inga Kuznetsova
"""
import numpy as np
from Heteroscedasticity_test_general import Heteroscedasticity_tests
class Glejser_test(Heteroscedasticity_tests):
     '''
     Glejser_test class tests heteroscedasticity computing p value for linear regression between function of feature in original regression under the test and 
     absolute value of residuals

     Attributes:
            numpy array X 
            numpy array Y
     '''
     def __init__(self, X=None, Y=None):
         Heteroscedasticity_tests.__init__(self, X, Y)
         #functions from feature for different linear regressions in Glejser test
         self.features = [np.abs(self.X), np.sqrt(np.abs(self.X)), np.reciprocal(np.abs(self.X))]
         #dictionary for xlabel from test number
         self.var_xlabel={1: '|x|', 2: 'sqrt(|x|)', 3: '1/|x|'}
         
         
     def choose_test(self):
        '''
         Function chooses regression for Glejser test with the best R2 score
         
         args:  none
         returns: maximum R2 score, and number of Glejser regression with this score, p value for this test
        '''
        scores=[]
        for j in range(len(self.features)):
            scores.append(self.find_p_value(self.features[j], self.y_new))
        #array with R2 scores
        R2s=[i[0] for i in scores]
        #array with p values
        pvalues =[i[1] for i in scores]
        #maximum R2 score
        mR2=max(R2s)
        #test wirh mR2
        n=R2s.index(mR2)+1
        del scores
        print("Test number {} works the best with R2={} and p value={}".format(n, mR2, pvalues[n-1]))
        return mR2, n, pvalues[n-1]
    
     def glejser_test(self):
         '''
         Function computes p value for Glejser test regression
         args:  none
         returns: p value to test slope for regression between considered feature and squared residuals. If p < 0.05 we rather have heteroscedasticity.
         '''
         R2, n, pvalue= self.choose_test()
         self.plot_data(self.X, self.Y, 'X', 'Y', title='original data')
        
         if pvalue > 0.00001:
            return "Glejser test: P value = {} is larger than 0.00001, you may not have Heteroscedasticity, check the Glejser test".format(pvalue)
         else:
            return "Glejser test: P value = {} is smaller than 0.00001, you have Heteroscedasticity".format(pvalue)
 
     def plot_test(self, n):
         """
         plots absolute value of residuals from feature for test number (int) n
         """
         self.plot_data(self.features[n-1], self.y_new, self.var_xlabel[n], '|residuals|', title = 'Glejser test  #{}'.format(n))
    
 