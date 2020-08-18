import Decision_Tree.file.loader as loader
import time as t
import random as r

class Settings:
    class console_output:
        Train_Data_loadtime = True
class Data:
    training_data = []
    def load_from_file(path):
        past = t.time()
        Data.training_data = loader.load_td_file(path)
        if Settings.console_output.Train_Data_loadtime:
            print(f'training data loaded in {round((t.time()-past)*1000)}ms')
    def load_example(code):
        if code == 1:
            Data.training_data = [
                ['Sunny', 'High', 'Weak', False], 
                ['Sunny', 'High', 'Strong', False], 
                ['Overcast', 'High', 'Weak', True], 
                ['Rain', 'High', 'Weak', True], 
                ['Rain', 'Normal', 'Weak', True], 
                ['Rain', 'Normal', 'Strong', False], 
                ['Overcast', 'Normal', 'Strong', True], 
                ['Sunny', 'High', 'Weak', False], 
                ['Sunny', 'Normal', 'Weak', True], 
                ['Rain', 'Normal', 'Weak', True], 
                ['Sunny', 'Normal', 'Strong', True], 
                ['Overcast', 'High', 'Strong', True], 
                ['Overcast', 'Normal', 'Weak', True], 
                ['Rain', 'High', 'Strong', False]
            ]
class Tree:
    def predict(data):
        if not Data.training_data == []:
            index = 0
            pure_found = False
            list_of_all = Data.training_data
            while not pure_found:
                counter = 0
                new_list = []
                for each in list_of_all:
                    if each[index] == data[index]:
                        new_list.append(each)
                        counter += -1*(-1*int(each[len(each)-1]))
                if not new_list == []:
                    list_of_all = new_list
                    pure_found = (counter == len(list_of_all))
                    if counter == 0:
                        break
                    index += 1
                else:
                    return bool(r.randint(0,1))
            return pure_found
        else:
            print('No training data loaded.')