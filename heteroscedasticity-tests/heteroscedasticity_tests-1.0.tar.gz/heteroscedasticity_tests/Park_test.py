# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 10:44:26 2020

@author: Inga Kuznetsova
"""
import numpy as np
from Heteroscedasticity_test_general import Heteroscedasticity_tests
class Park_test(Heteroscedasticity_tests):
     '''
     Park_test class tests heteroscedasticity computing p value for linear regression between feature in original regression under the test and squared residuals

     Attributes:
            numpy array X
            numpy array Y
     '''
     def __init__(self, X=None, Y=None):
         Heteroscedasticity_tests.__init__(self, X, Y)
         self.x = np.log(np.abs(self.X))
         #normalization helped to do P values more stable
         self.y=np.log(np.square(self.y_new)/(np.sum(np.square(self.y_new))/self.y_new.shape[0]))
         
     def park_test(self):
         '''
         Function computes p value for park test regression
         args:  none
         returns: p value to test slope for regression between considered feature and squared residuals. If p < 0.001 we rather have Heteroscedasticity.
         '''
         #considering logs as suggested
         self.plot_data(self.X, self.Y, 'X', 'Y', title='original data')
         pvalue = self.find_p_value(self.x, self.y)[1]
         if pvalue > 0.001:
            return "Park test: P value = {} is larger than 0.001, you may not have heteroscedasticity, check the Glejser test".format(pvalue)
         else:
            return "Park test: P value = {} is smaller than 0.001, you may have heteroscedasticity".format(pvalue)
        
     def plot_log_residuals(self):
         '''
         plots log(residuals^2) from log(|x|)
         '''
         self.plot_data(self.x, self.y, 'log(|X|)', 'log(residuals^2)', title='Park test')
            
 

        
   