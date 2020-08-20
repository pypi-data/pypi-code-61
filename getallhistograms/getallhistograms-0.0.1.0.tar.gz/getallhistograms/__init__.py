def histograms(data):
    import matplotlib.pyplot as plt
    cols=data.columns
    obj_cols=[]
    int_cols=[]
    for o in cols:
        if data[o].dtypes==object:
            obj_cols.append(o)
        else:
            int_cols.append(o)
    for m in range(len(int_cols)):
        x1=data[int_cols[m]].dropna()
        plt.title(str(int_cols[m]))
        plt.hist(x1)
        plt.show()
    for k in range(len(obj_cols)):
        x1=data[obj_cols[k]].dropna()
        x2=dict(x1.value_counts())
        names=list(x2.keys())
        if len(names)>=5:
            pass
        else:
            plt.title(str(obj_cols[k]))
            x1.value_counts().plot(kind='bar')
