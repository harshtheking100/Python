#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


print(pd.__version__)


# In[5]:


#Create Series



# In[6]:


lst=[11,12,13,14,15]
s=pd.Series(lst)
print(s)


# In[7]:


t=(11,12,13,14,15)
s=pd.Series(t)
print(s)


# In[8]:


ar= np.arange(1,20)
s=pd.Series(ar)
print(s)


# In[9]:


d={'a':10,'b':20,'c':30,'d':40}
s=pd.Series(d)
print(s)


# In[10]:


s.index #index values of your Series


# In[11]:


s.dtype #data type of Series


# In[12]:


s= pd.Series()#empty Series
s


# In[13]:


lst=[10,11,12,13,14]
s= pd.Series(data=lst,index=['a','b','c','d','e'])
print(s)


# In[14]:


s.min()


# In[15]:


s.max()


# In[16]:


s.sum()


# In[17]:


s.count()


# In[20]:


ar= np.arange(1,21)
s=pd.Series(ar)
print(s)


# In[21]:


s.head()


# In[22]:


s.head(3)


# In[23]:


s.tail()


# In[24]:


s.tail(2)


# In[25]:


s.info()


# In[28]:


s.describe


# In[ ]:





# In[27]:


s.describe()


# In[29]:


print(s)


# In[30]:


s[0]


# In[31]:


s[7]


# In[32]:


s[1:5]


# In[33]:


s.loc[4]


# In[34]:


s.loc[1:4]


# In[35]:


s.iloc[2]


# In[36]:


s.iloc[1:4]


# In[37]:


lst=[10,11,12,13,14]
s= pd.Series(data=lst,index=['a','b','c','d','e'])
print(s)


# In[38]:


s[0]


# In[39]:


s['b']


# In[40]:


s.loc['a']


# In[41]:


s.loc['a':'d']


# In[43]:


s.iloc[0:3]


# In[45]:


s[0:3]


# In[46]:


s['a':'d']


# In[47]:


lst=[10,11,12,13,14]
s= pd.Series(data=lst)
print(s)


# In[48]:


s.index='a','b','c','d','e'


# In[49]:


s


# In[50]:


s['e']=200 # update the value


# In[51]:


s


# In[53]:


s['k']=600 #add new value in Series


# In[54]:


s


# In[55]:


s['f']=1600


# In[56]:


s


# In[57]:


s+1


# In[58]:


s*3


# In[59]:


s%3


# In[60]:


s//4


# In[62]:


s[s>100] #Filter the value in Series


# In[63]:


s[s>100]=40


# In[64]:


s


# In[65]:


s=pd.Series([10,20,30,40,50],index=['a','b','c','d','e'])
s1=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(s)
print(s1)


# In[66]:


s+s1


# In[67]:


s-s1


# In[68]:


s//s1


# In[69]:


s['f']=100


# In[70]:


s


# In[71]:


s+s1


# In[73]:


np.add(s,s1)


# In[74]:


np.subtract(s,s1)


# In[75]:


np.multiply(s,s1)


# In[76]:


s.add(s1)


# In[ ]:





# In[78]:


s1.add(s,fill_value=0)


# In[79]:


s1.add(s,fill_value=10)


# In[80]:


s=pd.Series([10,20,30,40,50],index=['a','b','c','d','e'])
s1=pd.Series([1,2,3,4,5],index=[1,2,3,4,5])
print(s)
print(s1)


# In[81]:


s+s1


# In[82]:


s.add(s1,fill_value=10)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




