def piecharts(data):
    import matplotlib.pyplot as plt
    cols=data.columns
    obj_cols=[]
    for o in cols:
        if data[o].dtypes==object:
            obj_cols.append(o)
    names_list=[]
    vals2=[]
    new_cols=[]
    for k in range(len(obj_cols)):
        x1=data[obj_cols[k]].dropna()
        x2=dict(x1.value_counts())
        names=list(x2.keys())
        if len(names)>=30:
            pass
        else:
            new_cols.append(obj_cols[k])
            names_list.append(names)
        x3=list(x2.values())
        if len(x3)>=30:
            pass
        else:
            vals1=[]
            for i in range(len(x3)):
                vals=x3[i]
                vals1.append(vals)
            vals2.append(vals1)   
    nam2=[]
    for nam in names_list:
        names2=[]
        for k in nam:
            if type(k)!=str:
                names2.append(str(k))
            else:
                names2.append(k)
        nam2.append(names2)
    for c in range(len(vals2)):
        Tasks = vals2[c]
        my_labels = nam2[c]
        plt.pie(Tasks,labels=my_labels,autopct='%1.1f%%')
        plt.title(str(new_cols[c]))
        plt.axis('equal')
        plt.show()    