import pandas as pd
import datetime
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression
from .Client import Client

class Account(Client):
    """Class for manage client's balance, establish different types of clients and accounts, charge and apply interest.\n",
    "        
    "        Attributes
    "            client_name (string) represents clients name.
    "            age (int) represents client's age.
    "            balance (float) represents client's initially balance.
    "            client_id (int) represents client identification.
    "            client_joindate (datetime) represent time when the client account was created with established format Y/M/D.
    "            client_joindate2 (datetime) represent time when the client account was created in days.
    "            account_category (list of strings) represents the kind of account depending on the account time.
    "            client_category (list of strings) represents the type of client depending on their age.
        """
    def __init__(self):
        Client.__init__(self)
        self.account_category = []
        self.client_category = []
        
    def add_balance(self,client_id,balance):
        """  Function to sum new balance to a specific client ID.
    "        
    "        Args:
    "            client_id (int) represents the client identification number.
    "            
    "        Returns:
    "            int: The new client's balance
    "            
    "        """
        if client_id not in range(1,len(self.client_id)):
            return "Clinet_ID do not found, check your client ID again"
        else:
            self.balance[client_id] += balance
    
    def set_client_category(self):
        """  Function to set the client'scategory type depending on their age.
    "        
    "        Args:
    "            None
    "            
    "        Returns:
    "            None
    "            
    "        """
        for i in self.client_id:
            if self.age[i] > 50:
                self.client_category.append("Senior")
            elif self.age[i] <= 25:
                self.client_category.append("Junior")
            else:
                self.client_category.append("Regular")
    def set_account_category(self):
        """  Function to set the account 'scategory type depending on their creation date.
    "        
    "        Args:
    "            None
    "            
    "        Returns:
    "            None
    "            
    "        """
        # Add to the list in order whether their joindate and current date is higher than 300 days as Premium clients.
        for i in self.client_id:
            if (datetime.datetime.now() - self.joindate2[i] ).days > 300:
                self.account_category.append("Premium")
            else:
                self.account_category.append("Standard")
                
    def income_per_month(self,client_id):
        """  Function to return the average of the income per month of a client.
    "        
    "        Args:
    "            client_id (int) represents client identification.
    "            
    "        Returns:
    "            float: The client's balance / month.
    "            
    "        """
        # The difference btween the client's join date and the current date.
        day = datetime.datetime.now()- self.joindate2[client_id]
        
        return self.balance[client_id] / (day.seconds/60)
    
    def interest(self):
        """  Function to calculate the balance's interest based on the account_category.
    "        
    "        Args:
    "            None
    "            
    "        Returns:
    "            None
    "            
    "        """
        self.set_account_category()
        
        # Check for each client account type and add to the balance an interest based on the account_category.
        for i in self.client_id:
            if self.account_category[i] == "Premium":
                self.balance[i] += self.balance[i] * 0.06
            else:
                self.balance[i] += self.balance[i] * 0.03

    def charge(self):
        """  Function to calculate the charges applied on the account based on the client_category.
    "        
    "        Args:
    "            None
    "            
    "        Returns:
    "            None
    "            
    "        """
        self.set_client_category()
        
        # Check for each client client type and charge the balance based on the client_category.
        for i in self.client_id:
            if self.client_category[i] == "Junior":
                self.balance[i] -= 0
            elif self.client_category[i] == "Regular":
                self.balance[i] -= 30
            else:
                self.balance[i] -= 0
                
