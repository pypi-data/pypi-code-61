from apriorib.apriorib import Apriori

def main():
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
    df1,df2,df3,df4 = apr.show_as_df(stage=1),apr.show_as_df(stage=2),apr.show_as_df(stage=3),apr.show_as_df(stage=4)
    print("VIEWING THE ITEMSET DATAFRAMES AT THE DIFFERENT STAGES :\nSTAGE 1\n{}\nSTAGE 2\n{}\nSTAGE 3\n{}\nSTAGE 4\n{}".format(df1,df2,df3,df4))
    apr.checkAssc()

if __name__ == "__main__":
    main()