#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv("Food-Truck-LineReg.csv",header = None)
data.columns = ['x','y'] 


# In[3]:




data.head()


# In[4]:


n = data['x'].count()
print(n)


# In[5]:


x= data['x']
y= data['y']
y_sum = 0
x_sum = 0 
x2 = 0
y2 = 0
xy = 0
for i in range(n):
    x_sum += x[i]
    y_sum += y[i]
    x2 += (x[i]**2)
    y2 += (y[i]**2)
    xy += x[i]*y[i]
    
x_mean  = x_sum/n;
y_mean = y_sum/n;
dev_x = 0
dev_y = 0
for i in range(n):
    dev_x += ((x[i]-x_mean)**2)
    dev_y += ((y[i]-y_mean)**2)
x_std = (dev_x/n)**(1/2)
y_std = (dev_y/n)**(1/2)
print(x_std,y_std,x_mean,y_mean)


# In[6]:


r = (xy-(x_sum*y_sum)/n)/(((x2-(((x_sum)**2)/n))**(1/2))*((y2-(((y_sum)**2)/n))**(1/2)))
m = r*(y_std/x_std)
c = y_mean - m*x_mean
print(m,r,c)


# In[7]:


y_pred = []
for num in x:
    y_pred.append((m*num) + c)
data['y1']=y_pred
data.head()


# In[8]:


import matplotlib.pyplot as plt
plt.scatter(x,y)
plt.plot(x,y_pred,color='black')
plt.show()


# In[9]:


SSE = 0
SST = 0
SSR = 0
for i in range(n):
    SST += ((y[i] - y_mean)**2)
    SSE += ((y[i]-y_pred[i])**2)
    SSR += ((y_pred[i]-y_mean)**2)
MSE = SSE/n
cost = MSE**(1/2)
R2 = 1- (SSE/SST)
print("SST: {}\nSSE: {}\nSSR: {}\nMSE: {}\nCost: {}\nR2: {}".format(SST,SSE,SSR,MSE,cost,R2))


# In[ ]:




