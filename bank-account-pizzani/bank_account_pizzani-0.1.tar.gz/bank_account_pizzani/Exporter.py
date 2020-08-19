import pandas as pd
import datetime
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from .Account import Account

class Exporter(Account):
    """ Class to create dataframes if clients, export them and create graphs
    "        
    "        Attributes:
    "            client_name (string) represents clients name.
    "            age (int) represents client's age.
    "            balance (float) represents client's initially balance.
    "            client_id (int) represents client identification.
    "            client_joindate (datetime) represent time when the client account was created with established format Y/M/D.
    "            client_joindate2 (datetime) represent time when the client account was created in days.
    "            account_category (list of strings) represents the kind of account depending on the account time.
    "            client_category (list of strings) represents the type of client depending on their age.
    "            
    "         """
    def create_dataframe(self):
        """  Function to create a dataframe from the previously added clients.
    "        
    "        Args:
    "            None
    "            
    "        Returns:
    "            dataframe: A Data Frame containing client's data.
    "            
    "        """
        df = pd.DataFrame([self.client_id,self.client_name,self.age,self.balance,self.joindate,self.client_category,self.account_category]).T
        df.columns = ["client_id","client_name","age","balance","joindate","client_category","account_category"]
        df.index = self.client_id
        return df
        
    def LM(self):
        """  Function to create Linear Regression Model and return a graph containing the Linear model distribution.
    "        
    "        Args:
    "            None
    "            
    "        Returns:
    "            None
    "            
    "        """
        # Use function to create a cleint Data Frame.
        df = self.create_dataframe()
        
        # create a list of predicitons
        predictions= []
        
        # set X and Y axes using the Age and Balance columns from the data frame.
        x = df[["age"]]
        y = df[["balance"]]
        
        # create a Linear Regression Model and fit it with the data.
        model = LinearRegression()
        model.fit(x,y)
        
        # Add to the list of predictions the model balance predictions for each client age.
        for z in self.age:
            predictions.append(model.intercept_ + (model.coef_ * z))
        
        # plot the results.
        plt.scatter(self.age,self.balance)
        plt.plot(np.array(self.age).reshape(-1,1),np.array(predictions).reshape(-1,1), c="r")
        plt.xlabel("Age")
        plt.ylabel("Balance")
        plt.title("Linear Regression AGE vs Salary")
        plt.legend(["Linear Regression","Data"])   
    