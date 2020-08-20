# -*- coding: utf-8 -*-

# @Time    : 2020/8/20 14:37
# @Email   : 986798607@qq.com
# @Software: PyCharm
# @License: BSD 3-Clause

if __name__ == "__main__":
    # data
    from sklearn.datasets import load_boston

    data = load_boston()
    x = data["data"]
    y = data["target"]
    c = [6, 3, 4]

    sl = SymbolLearning(pop=50, gen=3, cal_dim=True, re_hall=2, add_coef=True, cv=2, random_state=1
                        )
    sl.fit(x, y, c=c, x_group=[[1, 3], [0, 2], [4, 7]])
    score = sl.score(x, y, "r2")
    print(sl.expr)
