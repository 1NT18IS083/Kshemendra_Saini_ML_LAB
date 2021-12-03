#!/usr/bin/env python
# coding: utf-8

# In[1]:


l = [1,2,3,4,5]
l.append("abc")


# In[2]:


print(l)


# In[4]:


l.pop(5)


# In[5]:


print(l)


# In[8]:


m =[6,7,8,9,10]


# In[9]:


result=l+m
print(result)


# In[10]:


for i in result:
    print(i)


# In[11]:


print(min(result))
print(max(result))
print(min(l))
print(max(l))
print(min(m))
print(max(m))


# In[2]:


a = 5
b = 7
print(a,b)
a,b = b,a
print(a,b)


# In[3]:


tupple=("ks","saini")
tupple


# In[5]:


dict={
    "ks":"1NT18IS083",
    "niraj":"1NT18IS197",
    "krishna":"1NT18IS195"
}
dict

