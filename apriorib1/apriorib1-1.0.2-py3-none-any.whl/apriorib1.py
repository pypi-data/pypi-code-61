import numpy as np 
import pandas as pd 
from itertools import combinations

class Apriori():
    def __init__(self,records,min_sup=2,min_conf=50):
        self.records = records
        self.min_sup = min_sup
        self.min_conf = min_conf

        self.items = sorted([item for sublist in self.records for item in sublist if item != np.nan])
    '''Function to check if for each subset of the current itemlist(k), whether the combination of k-1 items(previous grouping/pairing),
    belongs to the previous itemlist, so that it qualifies to be a frequent itemlist. 
    Arguments : current itemlist, previous itemlist, n(= k-1)'''
    def checkFreq(self,prev,curr,n=1):
        if n > 1:
            subsets = list(combinations(curr,n))
        else:
            subsets = prev
        for item in subsets:
            if not item in subsets:
                return False
            else:
                return True
    '''Function to check if i1 is a sublist/subset of i2'''
    def sublist(self,it1,it2):
        return set(it1) <= set(it2)
    # Stage 1
    def stage_1(self,itemlist,min_sup):
        c1 = {i: itemlist.count(i) for i in itemlist}
        l1 = {}
        for key,val in c1.items():
            if val >= min_sup:
                l1[key] = val
        return c1,l1
    # Stage 2
    def stage_2(self,l1,records,min_sup):
        l1 = sorted(list(l1.keys()))
        L1 = list(combinations(l1,2))
        c2,l2 = {},{}
        for it1 in L1:
            count = 0
            for it2 in records:
                if self.sublist(it1,it2):
                    count += 1
            c2[it1] = count
        for key,val in c2.items():
            if val >= min_sup:
                if self.checkFreq(key,l1,1):
                    l2[key] = val
        return c2,l2
    # Stage 3
    def stage_3(self,l2,records,min_sup):
        l2 = sorted(list(l2.keys()))
        L2 = sorted(list(set([item for temp in l2 for item in temp])))
        L2 = list(combinations(L2,3))
        c3,l3 = {},{}
        for it1 in L2:
            count = 0
            for it2 in records:
                if self.sublist(it1,it2):
                    count += 1
            c3[it1] = count
        for key,val in c3.items():
            if val >= min_sup:
                if self.checkFreq(key,l2,2):
                    l3[key] = val
        return c3,l3
    # Stage 4
    def stage_4(self,l3,records,min_sup):
        l3 = sorted(list(l3.keys()))
        L3 = sorted(list(set([item for temp in l3 for item in temp])))
        L3 = list(combinations(L3,4))
        c4,l4 = {},{}
        for it1 in L3:
            count = 0
            for it2 in records:
                if self.sublist(it1,it2):
                    count += 1
            c4[it1] = count
        for key,val in c4.items():
            if val >= min_sup:
                if self.checkFreq(key,l3,3):
                    l4[key] = val
        return c4,l4
    # Preparing data for displaying stage wise lookup tables + support scores
    def show_as_df(self,stage=2):
        c1,l1 = self.stage_1(self.items,self.min_sup)
        c2,l2 = self.stage_2(l1,self.records,self.min_sup)
        c3,l3 = self.stage_3(l2,self.records,self.min_sup)
        c4,l4 = self.stage_4(l3,self.records,self.min_sup)
        # Display as dataframes
        if stage == 1:
            df_stage1 = pd.DataFrame(l1,index=['sup_count']).T
            return df_stage1
        elif stage == 2:
            df_stage2 = pd.DataFrame(l2,index=['sup_count']).T
            return df_stage2
        elif stage == 3:
            df_stage3 = pd.DataFrame(l3,index=['sup_count']).T
            return df_stage3
        else:
            df_stage4 = pd.DataFrame(l4,index=['sup_count']).T
            return df_stage4
    # Create complete itemlist
    def create_itemlist(self):
        c1,l1 = self.stage_1(self.items,self.min_sup)
        c2,l2 = self.stage_2(l1,self.records,self.min_sup)
        c3,l3 = self.stage_3(l2,self.records,self.min_sup)
        c4,l4 = self.stage_4(l3,self.records,self.min_sup)

        itemlist = {**l1,**l2,**l3,**l4}
        return itemlist
    def supCalc(self,it1,itemlist):
        return itemlist[it1]
    # Function to accept/reject association rules
    def checkAssc(self):
        min_c = self.min_conf
        c1,l1 = self.stage_1(self.items,self.min_sup)
        c2,l2 = self.stage_2(l1,self.records,self.min_sup)
        c3,l3 = self.stage_3(l2,self.records,self.min_sup)
        l3_assc = list(l3.keys())
        iteml = self.create_itemlist()
        assc_set = []
        for it1 in list(l3.keys()):
            assc_subset = list(combinations(it1,2))
            assc_set.append(assc_subset)
        # Association rule mining
        '''Implementing the association rule.
        An association rule is formed iff the confidence of that rule exceeds the minimum confidence threshold.
        Assuming minimum confidence = 50% (Default, unless otherwise mentioned)
        '''
        for i in range(len(l3_assc)):
            for it1 in assc_set[i]:
                denom = it1
                d = list(denom)
                numer = set(l3_assc[i]) - set(it1)
                n = list(numer)
                confidence = ((self.supCalc(l3_assc[i],iteml))/(self.supCalc(it1,iteml)))*100
                if confidence > min_c:
                    print("Confidence of the association rule {} --> {} = {:.2f}%".format(denom,numer,confidence))
                    print("STATUS : SELECTED RULE\n* People who buy {} and {} also tend to buy : {} *\n".format(d[0],d[1],n[0]))
                else:
                    print("Confidence of the association rule {} --> {} = {:.2f}%".format(denom,numer,confidence))
                    print("STATUS : REJECTED RULE\n")

'''if __name__ == "__main__":
    data = [['MILK', 'BREAD', 'BISCUIT'],
    ['BREAD', 'MILK', 'BISCUIT', 'CORNFLAKES'],
    ['BREAD', 'TEA', 'BOURNVITA'],
    ['JAM', 'MAGGI', 'BREAD', 'MILK'],
    ['MAGGI', 'TEA', 'BISCUIT'],
    ['BREAD', 'TEA', 'BOURNVITA'],
    ['MAGGI', 'TEA', 'CORNFLAKES'],
    ['MAGGI', 'BREAD', 'TEA', 'BISCUIT'],
    ['JAM', 'MAGGI', 'BREAD', 'TEA'],
    ['BREAD', 'MILK'],
    ['COFFEE', 'COCK', 'BISCUIT', 'CORNFLAKES'],
    ['COFFEE', 'COCK', 'BISCUIT', 'CORNFLAKES'],
    ['COFFEE', 'SUGER', 'BOURNVITA'],
    ['BREAD', 'COFFEE', 'COCK'],
    ['BREAD', 'SUGER', 'BISCUIT'],
    ['COFFEE', 'SUGER', 'CORNFLAKES'],
    ['BREAD', 'SUGER', 'BOURNVITA'],
    ['BREAD', 'COFFEE', 'SUGER'],
    ['BREAD', 'COFFEE', 'SUGER'],
    ['TEA', 'MILK', 'COFFEE', 'CORNFLAKES']]
    
    # Testing the Apriori class
    apr = Apriori(records=data,min_sup=2,min_conf=50)
    df_stage4 = apr.show_as_df(stage=4)
    print(df_stage4)
    apr.checkAssc()'''
