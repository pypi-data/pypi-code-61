# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 15:06:07 2020

@author: Peng Shangguan
"""

# 规整与总结代码，并封装成常用函数
# In[]
'''
目录
画图函数
数据读取函数
数据预处理函数
模型函数
量化指标计算
因子测试框架

'''
# In[导包]
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.dates as mdate
from matplotlib import dates as mdates
import matplotlib.ticker as ticker
from matplotlib.pyplot import MultipleLocator
from matplotlib.font_manager import FontManager, FontProperties
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
plt.rcParams['axes.unicode_minus'] = False  # 显示负号
plt.rcParams['savefig.dpi'] = 600 #图片像素
plt.rcParams['figure.dpi'] = 1080 #分辨率
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import statsmodels.api as sm
import scipy.stats as st
import os
import tables
from dateutil.parser import parse
# In[]
# 画图函数 #
def get_figure(df,file='./fig.png',option=1,figsize=(24, 10),color='blue',fontsize=24,linewidth=3,figsquare=(0.05,0.95,0.95,0.05)):
    '''
    

    Parameters
    ----------
    df : TYPE
        DESCRIPTION.
    file : TYPE
        DESCRIPTION. 保存路径
    option : TYPE, optional
        DESCRIPTION. The default is 1.
        1 ->多线条-以列名作为label
    figsize : TYPE, optional
        DESCRIPTION. The default is (24, 10).
    gridspec : TYPE, optional
        DESCRIPTION. The default is (1,1).
    fontsize : TYPE, optional
        DESCRIPTION. The default is 24.
    linewidth : TYPE, optional
        DESCRIPTION. The default is 3.

    Returns
    -------
    None.

    '''
    matplotlib.rcParams.update({'font.size': fontsize})
    blue = ['darkblue','b','slateblue','lightsteelblue','lavender','r']
    purple = ['indigo','purple','mediumpurple','orchid']
    if color=='blue':
        c = blue
    elif color=='purple':
        c = purple
    else:
        c = blue
    fig = plt.figure(figsize=figsize)
    gs = fig.add_gridspec(1, 1)
    f_ax1 = fig.add_subplot(gs[0, 0])
    s = len(df.columns)
    for i in range(s):
        f_ax1.plot(df[df.columns[i]],color=c[i],linewidth=linewidth,label=df.columns[i])
    f_ax1.legend(loc='upper center',bbox_to_anchor=(0.5,1.05),frameon=False,ncol=s)
    f_ax1.spines['top'].set_visible(False)
    f_ax1.spines['right'].set_visible(False)
    f_ax1.spines['bottom'].set_linewidth(1.5)###设置底部坐标轴的粗细
    f_ax1.spines['left'].set_linewidth(1.5)####设置左边坐标轴的粗细
    f_ax1.spines['right'].set_linewidth(1.5)####设置右边坐标轴的粗细
    plt.tick_params(labelsize=fontsize)
    plt.subplots_adjust(left=figsquare[0], right=figsquare[1], top=figsquare[2], bottom=figsquare[3], wspace=0.2, hspace=0.15)
    plt.savefig(file)

# In[]
# 数据读取函数 #
def csv(path):
    '''
    

    Parameters
    ----------
    path : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    df = pd.read_csv(path,index_col=0,encoding='gbk')
    df.index = pd.to_datetime(df.index)
    return df
def xlsx(path):
    df = pd.read_excel(path,index_col=0,encoding='gbk')
    df.index = pd.to_datetime(df.index)
    return df

def get_filename(path):
    return os.listdir(path)
   

# In[]
# 数据预处理函数 #
def three_sigma(factor):
    '''
    

    Parameters
    ----------
    factor : TYPE
        DESCRIPTION.第T期所有因子序列

    Returns
    -------
    factor : TYPE
        DESCRIPTION.

    '''
    mean = np.mean(factor)
    std = np.std(factor)
    high = mean+3*std
    low = mean-3*std
    factor = np.where(factor>high,high,factor)
    factor = np.where(factor<low, low, factor)
    return factor

def stand(factor):
    '''
    

    Parameters
    ----------
    factor : TYPE
        DESCRIPTION.第T期所有因子序列

    Returns
    -------
    factor : TYPE
        DESCRIPTION.

    '''
    mean = np.mean(factor)
    std = np.std(factor)
    return (factor-mean)/std



# In[]
# 模型函数 #





# In[]
# 量化指标计算 #
def cal_culr(r):
    '''
    

    Parameters
    ----------
    r : TYPE
        DESCRIPTION.收益率序列

    Returns
    -------
    cul_r : TYPE
        DESCRIPTION.净值序列

    '''
    cul_r = pd.DataFrame(index=r.index,columns=r.columns) 
    cul_r.loc[cul_r.index[0],:] = 1
    for i in range(len(r)-1):
         cul_r.loc[cul_r.index[i+1],:] = cul_r.loc[cul_r.index[i],:]*(1+r.loc[r.index[i+1],:])
    return cul_r

def cal_ret(r):
    
    cul_r = pd.DataFrame(index=r.index,columns=r.columns) 
    cul_r.loc[cul_r.index[0],:] = 1
    for i in range(len(r)-1):
         cul_r.loc[cul_r.index[i+1],:] = cul_r.loc[cul_r.index[i],:]*(1+r.loc[r.index[i+1],:])
    result = pd.DataFrame(index=r.columns)
    n = len(r)
    for i in range(len(r.columns)):
        result.loc[r.columns[i],'择时年化收益'] = '%.2f%%'%((cul_r.loc[cul_r.index[-1],cul_r.columns[i]]**(252/n)-1)*100)
        vol = ((252/(n-1))*((r[r.columns[i]]-r[r.columns[i]].mean())**2).sum())**0.5
        result.loc[r.columns[i],'策略收益波动'] = '%.2f%%'%(vol*100)
        data = cul_r[cul_r.columns[i]]
        index_j = (np.maximum.accumulate(data) - data).astype(float).idxmax() # 结束位置
        index_i = (data[:index_j]).astype(float).idxmax() # 开始位置
        d = (data[index_j] - data[index_i])/data[index_i]  # 最大回撤
        result.loc[r.columns[i],'最大回撤'] = '%.2f%%'%(d*100)
        result.loc[r.columns[i],'夏普比率'] = '%.2f'%(((cul_r.loc[cul_r.index[-1],cul_r.columns[i]]**(252/n)-1))/vol)
        win = 1-len(r[r[r.columns[i]]<0])/len(r)
        result.loc[r.columns[i],'胜率'] = '%.2f%%'%(win*100)
    return result

# In[]
# 因子测试框架 #
def factor_regress(df,industry):
    '''
    因子收益
    以未来收益作为被解释变量，以因子值、行业虚拟变量和市值作为解释变量

    Parameters
    ----------
    df : TYPE
        DESCRIPTION.包含未来收益next_ret、因子值factor、市值value,且索引为date+code
    industry : TYPE
        DESCRIPTION.股票池内代码和行业分类

    Returns 
    -------
    因子收益测试结果

    '''
    t = []
    r_factor = []
    date = df.index.get_level_values(0).unique()
    for i in date:
        _ = df.loc[i,:]
        _ = _.dropna(axis=0)
        if _.empty:
            continue
        if len(_)<30:
            continue
        _['factor'] = three_sigma(_['factor'])
        _['factor'] = stand(_['factor'])
        _.loc[_.index, 'ind']=industry.loc[_.index,'ind']
        dummy_ind = pd.get_dummies(_['ind'])
        y = _['next_ret']
        x = pd.concat([_[['factor','value']],dummy_ind],axis=1)
        x = sm.add_constant(x)
        model = sm.WLS(y,x,weights=np.sqrt(_['value'])).fit()
        t.append(model.tvalues[1])
        r_factor.append(model.params[1])
    # 统计因子评价指标
    result = pd.DataFrame(index = ['factor'])
    t = pd.DataFrame(t,columns=['t'])
    t_mean = abs(t['t']).mean()
    t_p = len(t[t['t']>2])/len(t['t'])
    result.loc['factor','t值绝对值平均值'] = t_mean
    result.loc['factor','t>2概率'] = '%.2f%%'%(t_p*100)
    r_factor = pd.DataFrame(r_factor,columns=['r_factor'])
    r_mean = r_factor['r_factor'].mean()
    r_std = r_factor['r_factor'].std()
    result.loc['factor','因子收益平均值'] = r_mean
    result.loc['factor','因子收益标准差'] = r_std 
    return result

def neutralize(df,industry):
    '''
     行业市值中性化

    Parameters
    ----------
    df : TYPE
        DESCRIPTION.包含未来收益next_ret、因子值factor、市值value,且索引为date+code
    industry : TYPE
        DESCRIPTION.股票池内代码和行业分类
    Returns
    -------
    df : TYPE
        DESCRIPTION.在以上基础上添加了中性化后的因子 error

    '''
    date = df.index.get_level_values(0).unique()
    df['error'] = df['factor']
    for i in date:
        _ = df.loc[i,:]
        _ = _.dropna(axis=0)
        if _.empty:
            continue
        if len(_)<30:
            continue
        # 去极值和标准化
        _['factor'] = three_sigma(_['factor'])
        _['factor'] = stand(_['factor'])
        _.loc[_.index, 'ind']=industry.loc[_.index,'ind']
        dummy_ind = pd.get_dummies(_['ind'])
        y = _['factor']
        x = pd.concat([_[['value']],dummy_ind],axis=1)
        x = sm.add_constant(x)
        model = sm.OLS(y,x)
        results = model.fit()
        df.loc[i].loc[_.index,'error'] = results.resid
    return df


def ic(df):
    '''
    

    Parameters
    ----------
    df : TYPE
        DESCRIPTION.包含未来收益next_ret、因子值factor、市值value、中性化后的因子error,且索引为date+code

    Returns
    -------
    result : TYPE
        DESCRIPTION.IC测试结果

    '''
    ic = []
    date = df.index.get_level_values(0).unique()
    for i in date:
        _= df.loc[i,:].dropna(axis=0)
        if _.empty:
            continue
        if len(_)<30:
            continue
        ic.append(st.spearmanr(_['error'].rank(),_['next_ret'])[0])
    ic = pd.DataFrame(ic,columns=['ic'])
    ic_mean = ic['ic'].mean()
    ic_std = ic['ic'].std()
    icir = ic_mean/ic_std
    ic_p = len(ic[ic['ic']>0])/len(ic['ic'])
    result = pd.DataFrame(index = ['factor'])
    result.loc['factor','IC平均值'] = ic_mean
    result.loc['factor','IC标准差'] = ic_std
    result.loc['factor','IRIC'] = icir
    result.loc['factor','IC>0概率'] = '%.2f%%'%(ic_p*100)
    return result

def group_test(df):
    
    df = df.reset_index(level=1)
    date = df.index.get_level_values(0).unique()
    
    for i in date:
        if len(df.loc[i,:])<30:
            continue
        bins = [df.loc[i,'error'].quantile(0),df.loc[i,'error'].quantile(0.2),df.loc[i,'error'].quantile(0.4),df.loc[i,'error'].quantile(0.6),df.loc[i,'error'].quantile(0.8),df.loc[i,'error'].quantile(1)]
        labels = ['G1','G2','G3','G4','G5']
        df.loc[i, 'group'] = pd.cut(df.loc[i,'error'],bins,labels=labels)
    
    df = df.reset_index()
    group_r = df.groupby(['date','group']).mean()['next_ret'].unstack()
    group_r['多空组合'] = group_r['G5']-group_r['G1']
    
    return group_r


