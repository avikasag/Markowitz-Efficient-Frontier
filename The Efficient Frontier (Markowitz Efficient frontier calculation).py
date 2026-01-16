#!/usr/bin/env python
# coding: utf-8

# ## Obtaining the Efficient Frontier 

# The Markowitz Efficient Frontier shows the set of portfolios that maximize expected return for a given level of risk (variance/volatility), or equivalently minimize risk for a given expected return, using asset means, variances, and covariances.

# For two companies (Stocks)
# ***

# In[1]:


import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

assets = ['WMT', 'FB']
pf_data = pd.DataFrame()

for a in assets:
    pf_data[a] = yf.Ticker(a).history(start='2014-1-1')['Close']


# In[2]:


log_returns = np.log(pf_data / pf_data.shift(1))

num_assets = len(assets)

weights = np.random.random(num_assets)
weights /= np.sum(weights)               #Normalizes (scales) the random weights so they add up to exactly 1 (100%)
weights


# In[3]:


weights[0] + weights[1]


# Now, estimate the expected Portfolio Return, Variance, and Volatility.

# Expected Portfolio Return:

# In[4]:


np.sum(weights * log_returns.mean()) * 250


# Expected Portfolio Variance:

# In[5]:


np.dot(weights.T, np.dot(log_returns.cov() * 250, weights))


# Expected Portfolio Volatility (Standard Deviation):

# In[6]:


np.sqrt(np.dot(weights.T,np.dot(log_returns.cov() * 250, weights)))


# ***

# # Markowitz Efficient frontier calculation
# 1)	Create two empty lists. Name them pf_returns and pf_volatilites.

# In[7]:


pf_returns = []
pf_volatilities = []


# 2)	Create a loop with 1,000 iterations that will generate random weights, summing to 1, and will append the obtained values for the portfolio returns and the portfolio volatilities to pf_returns and pf_volatilities, respectively.

# In[8]:


for x in range (1000):
    weights = np.random.random(num_assets)
    weights /= np.sum(weights)
    pf_returns.append(np.sum(weights * log_returns.mean()) * 250)
    pf_volatilities.append(np.sqrt(np.dot(weights.T,np.dot(log_returns.cov() * 250, weights))))
    
pf_returns, pf_volatilities


# 3)	Transform the obtained lists into NumPy arrays and reassign them to pf_returns and pf_volatilites. Once we have done that, the two objects will be NumPy arrays. 

# In[9]:


pf_returns = np.array(pf_returns)
pf_volatilities = np.array(pf_volatilities)

pf_returns, pf_volatilities


# Now, create a dictionary, called portfolios, whose keys are the strings “Return” and “Volatility” and whose values are the NumPy arrays pf_returns and pf_volatilities. 

# In[10]:


portfolios = pd.DataFrame({'Return': pf_returns, 'Volatility': pf_volatilities})


# In[11]:


portfolios.head()


# Finally, plot the data from the portfolios dictionary on a graph. Let the x-axis represent the volatility data from the portfolios dictionary and the y-axis – the data about rates of return. <br />
# Organize the chart well and make sure we have labeled both the x- and the y- axes.

# In[12]:


portfolios.plot(x='Volatility', y='Return', kind='scatter', figsize=(10, 6));
plt.xlabel('Expected Volatility')
plt.ylabel('Expected Return')


# ******

# For 3 companies or n-nukmber of companies (Stocks)
# 
# What would happen if we re-created the Markowitz Efficient Frontier for 3 stocks? 
# ***

# In[13]:


assets = ['WMT', 'META', 'BP']
pf_data = pd.DataFrame()

for a in assets:
    pf_data[a] = yf.Ticker(a).history(start='2014-1-1')['Close']


# In[14]:


pf_data.head()


# In[15]:


log_returns = np.log(pf_data / pf_data.shift(1))


# In[16]:


num_assets = len(assets)
num_assets


# In[19]:


weights = np.random.random(num_assets)
weights /= np.sum(weights)
weights


# In[20]:


weights[0] + weights[1] + weights[2]


# Expected Portfolio Return:

# In[21]:


np.sum(weights * log_returns.mean()) * 250


# Expected Portfolio Variance:

# In[22]:


np.dot(weights.T, np.dot(log_returns.cov() * 250, weights))


# Expected Portfolio Volatility:

# In[23]:


np.sqrt(np.dot(weights.T,np.dot(log_returns.cov() * 250, weights)))


# *****

# In[24]:


pfolio_returns = []
pfolio_volatilities = []

for x in range (1000):
    weights = np.random.random(num_assets)
    weights /= np.sum(weights)
    pfolio_returns.append(np.sum(weights * log_returns.mean()) * 250)
    pfolio_volatilities.append(np.sqrt(np.dot(weights.T,np.dot(log_returns.cov() * 250, weights))))
    
pfolio_returns = np.array(pfolio_returns)
pfolio_volatilities = np.array(pfolio_volatilities)

pfolio_returns, pfolio_volatilities


# In[25]:


portfolios = pd.DataFrame({'Return': pfolio_returns, 'Volatility': pfolio_volatilities})


# In[26]:


portfolios.plot(x='Volatility', y='Return', kind='scatter', figsize=(10, 6));
plt.xlabel('Expected Volatility')
plt.ylabel('Expected Return')


# In[ ]:




