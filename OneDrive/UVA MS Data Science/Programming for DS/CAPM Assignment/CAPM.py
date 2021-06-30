#!/usr/bin/env python
# coding: utf-8

# ## Walter Coleman txx3ej June 30, 2021

# In[1]:


# load modules
import numpy as np
import pandas as pd

# risk-free Treasury rate
R_f = 0.0175 / 252


# In[2]:


# read in the market data
data = pd.read_csv('capm_market_data.csv')


# In[3]:


data[['spy_adj_close', 'aapl_adj_close']]


# In[4]:


data.drop('date',axis=1, inplace=True)


# In[5]:


# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pct_change.html


# In[6]:


daily_returns = data.pct_change()[1:]


# In[7]:


daily_returns.head()


# In[8]:


spy_returns = np.array(daily_returns['spy_adj_close'])
aapl_returns = np.array(daily_returns['aapl_adj_close'])
print(spy_returns[:5])
print(aapl_returns[:5])


# In[9]:


excess_ret_spy = spy_returns - R_f
excess_ret_aapl = aapl_returns - R_f


# In[10]:


print(excess_ret_spy[-5:])
print(excess_ret_aapl[-5:])


# In[11]:


import matplotlib.pyplot as plt

plt.title('Excess Returns')
plt.xlabel('SPY Excess Returns')
plt.ylabel('AAPL Excess Returns')
plt.scatter(x=excess_ret_spy, y=excess_ret_aapl)


# In[12]:


# https://numpy.org/doc/stable/reference/generated/numpy.transpose.html
# https://numpy.org/doc/stable/reference/generated/numpy.matmul.html


# In[13]:


x_tr = np.transpose(excess_ret_spy)
x_tr_times_x = np.matmul(x_tr, excess_ret_spy)
x_tr_times_y = np.matmul(x_tr, excess_ret_aapl)
beta_est = (x_tr_times_x**-1)*x_tr_times_y
beta_est


# In[14]:


type(beta_est)


# In[15]:


x = excess_ret_spy
y = excess_ret_aapl


# In[16]:


def beta_sensitivity(x, y):
    """computes beta estimate"""
    
    results = []
    
    for i in range(len(x)):
        
        a = np.delete(x, i).reshape(-1,1) 
        b = np.delete(y, i).reshape(-1,1) 
        
        x_tr = np.transpose(a)
        x_tr_times_x = np.matmul(x_tr, a)
        x_tr_times_y = np.matmul(x_tr, b)
        beta_est = (x_tr_times_x**-1)*x_tr_times_y
        
        results.append( (i, beta_est[0][0]) )
    
    return results


# In[17]:


betas = beta_sensitivity(x, y)
betas[:5]

