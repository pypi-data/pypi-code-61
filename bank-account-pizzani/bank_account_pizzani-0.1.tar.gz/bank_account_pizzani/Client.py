import datetime
import pandas as pd


class Client:
    """ This Class input Bank's clients.
        
        Attributes:
            client_name (string) represents clients name.
            age (int) represents client's age.
            balance (float) represents client's initially balance.
            client_id (int) represents client identification.
            client_joindate (datetime) represent time when the client account was created with established format Y M D
            client_joindate2 (datetime) represent time when the client account was created in days.
            
        """

    def __init__(self, client_name ="Test", age=0, balance=0,joindate=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),joindate2= datetime.datetime.now()):
        # Lists of clients's data.
        self.client_id = [0]
        self.client_name = [client_name]
        self.age = [age]
        self.balance = [balance]
        self.joindate = [joindate]
        self.joindate2 = [joindate2]
        

        
    def add_client(self,client_name,age,balance,joindate=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),joindate2=datetime.datetime.now()):
        """ Function to add new clients atributes to the Class object.
        
        Attributes:
            client_joindate (datetime) represent time when the client account was created with established format Y M D
            client_joindate2 (datetime) represent time when the client account was created in days.
        
        
        Args:
            client_name (sting): The new client's name
            age (int): the new client's age
            balance (float): The new client's account balance.
            
        Returns:
            None
            
        """        
        
        # Adding plus 1 to the index of client's ID.\n",
        self.client_id.append(self.client_id[-1] + 1)
        
        self.client_name.append(client_name)
        self.age.append(age)
        self.balance.append(balance)
        self.joindate.append(joindate)
        self.joindate2.append(joindate2)
        
    def read_csv(self,file,joindate=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),joindate2=datetime.datetime.now()):
        """Function to add new clients atributes to the Class object through a CSV file without header.
    "        
    "        Attributes:
    "            client_joindate (datetime) represent time when the client account was created with established format Y M D\n",
    "            client_joindate2 (datetime) represent time when the client account was created in days.
    "            data (data) extarcted form the "file" data.
    "        
    "        
    "        Args:
    "            file (csv, data list): A CSV file that contains client_name, age and balance
    "            
    "        Returns:
                    None 
                    """
        # reads the csv file.
        self.data = pd.read_csv(file,header=None)
        
        # Range to calculate client ID from the length of the data set.
        self.client_id = [x for x in range(0,len(self.data))]
        
         # Data from the three columns in the CSV file.
        self.client_name = self.data[0].values.tolist()
        self.age = self.data[1].values.tolist()
        self.balance = self.data[2].values.tolist()
        
        # Set Time the clients were added to the Class.
        self.joindate = [joindate for x in range(len(self.data))]
        self.joindate2 = [joindate2 for x in range(len(self.data))]
        