def getresults_levelwise(df, i, level, res):
    res4 = []
    for r in range(res.shape[0]):
        res4.append(sum(res.iloc[r, :]) / res.shape[1])
    x = df.iloc[:, i]
    cc1 = []
    for j in range(1, level + 1):
        cc = []
        cc1.append(cc)
        for p in range(x.shape[0]):
            if x[p] == j:
                cc.append(res4[p])
    sql = []
    for l in range(len(cc1)):
        sql.append(sum(cc1[l]) / len(cc1[l]))
    return (sql)
