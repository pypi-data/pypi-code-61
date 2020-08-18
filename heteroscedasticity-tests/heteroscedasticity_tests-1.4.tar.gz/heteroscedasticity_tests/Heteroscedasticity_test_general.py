# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 12:38:37 2020

@author: Inga Kuznetsova
"""

import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
class Heteroscedasticity_tests():
      """ Generic class for Heteroscedasticity tests as
            Park and Glejser methods.
            Both methods use linear regression for functions of tested income feature and residuals as outcome
    
        Attributes:
            numpy arrays X, Y
            if you use pandas dataframe df
            X = df['x'].values.reshape(-1,1)
            Y = df['y'].values.reshape(-1,1)
      """
      def __init__(self, X, Y):
         #incoming feature
         self.X = X
         #outcome
         self.Y = Y
         #residuals
         self.y_new=self.find_residuals()
         
        
      def fit_results(self, x, y):
          '''
          fit linear model 
          args: x, y
          returns: model
          '''
          model=sm.regression.linear_model.OLS(x, y)
          return model.fit()
      
      def find_residuals(self):
          '''
          function computes linear regression residuals
          args:
              regression incoming features: x
              regression outcome: y
          returns: residuals
          '''
         # model = lm.LinearRegression()
         # model.fit(self.X, self.Y)
         # Y_pred = model.predict(self.Y)
          return np.abs(self.fit_results(self.X, self.Y).resid)
      
      def find_p_value(self, x, y):
          '''
          computes p value for regression between x and y
          args: x and y, income and outcome for linear regression
          returns: p value
          '''
        
          results = self.fit_results(x, y)
         
          return results.rsquared, results.pvalues[0]
      
      def plot_data(self, x, y, xlabel, ylabel, title=None):

        """Function to plot original data
        
        Args:
           x and y to plot, xlabel, ylabel, title
        Produces:
            plot
            
        """
        # make the plot
        plt.scatter(x, y)
        plt.ylabel(ylabel)
        plt.xlabel(xlabel)
        plt.title(title)
      
        plt.show()

        
        
        
         
    