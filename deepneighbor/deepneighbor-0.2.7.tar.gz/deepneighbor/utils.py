import networkx as nx
import itertools
import random
import pandas as pd


def generate_sentences(data):
    '''
    input dataframe.
      user  item
    	1	a
    	1	b
    	1	c
    	2	d
    	2	a
    output sentences. [user_id1, all_item(1...k1),user_id2,all_item(1...k2),...]
    [1,a,b,c,2,d,a]
    '''
    out = []
    data = pd.read_csv(data,sep=' ',header=None)

    data.columns = ['user','item']
    print(data.head())
    data['item'] = data['item'].astype(str)
    data['user'] = data['user'].astype(str)
    for user in data.user.unique():
        temp = [user]
        temp.extend(data[data.user == user].item.unique().tolist())
        out.append(temp)
    return out

def convert_to(data,le):
    '''
    given txt or csv file
    transform with label encoder
    return dataframe with two columns [from] and [to]
    '''

    data = pd.read_csv(data)
    data.columns = ['user','item']
    le.fit(data.user.unique().tolist()+data.item.unique().tolist())
    for col in data.columns:
        data[col] = le.transform(data[col])
    return data,le




def generate_sentences_dw(data):
    return nx.read_edgelist(data,)
