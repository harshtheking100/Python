#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[3]:


d={'a':[1,2,3,4,None],'b':[10,20,None,4,6],'c':[100,None,200,300,500],'d':[110,120,20,30,50]}
df=pd.DataFrame(d)
df


# In[4]:


df.columns


# In[5]:


df.columns=['aa', 'bb', 'cc', 'dd'] #rename cols
df


# In[7]:


df.rename(columns={'aa':'a', 'bb':'b', 'cc':'c'},inplace=True) #selective rename
df


# In[8]:


df


# In[9]:


df.dropna() #delete rows having Nan Values


# In[10]:


print(df)
df.dropna(axis=0)


# In[11]:


print(df)
df.dropna(axis=1)#delete all cols having nan


# In[12]:


print(df)
df.fillna(0)


# In[13]:


print(df)
df.fillna(10)


# In[14]:


print(df)
df.fillna(df["dd"].mean())


# In[15]:


print(df)
df.fillna(df.loc[0].mean())


# In[16]:


df["a"]


# In[17]:


df["a"].isnull() #checking for col


# In[18]:


df.loc[1].isnull()  #checking for row


# In[24]:


pd.isnull(df.loc[1,"c"]) #to check for Single Value


# In[25]:


df


# In[26]:


df.replace({4.0:40})


# In[27]:


df["dd"].replace(20,200)


# In[28]:


exam_data  = {'name': ['Sonu', 'Raja', 'Ketaki', 'Rupa', 'Radha', 'Reshma', 'Keshav', 'Narendra', 'Rani', 'Kittu'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df= pd.DataFrame(exam_data,index=labels)
df


# In[29]:


df["qualify"]


# In[30]:


df["qualify"].replace({'yes':True,'no':False})


# In[31]:


df["qualify"]=df["qualify"].map({'yes':True,'no':False})


# In[32]:


df


# In[33]:


d={'id':[1,2,3],'name':['kirti','rashmi','rakesh']}
d1={'id':[1,2,4],'age':[12,34,57]}
df=pd.DataFrame(d)
df1=pd.DataFrame(d1)
print(df)
print(df1)


# In[34]:


pd.merge(df,df1,on='id')


# In[35]:


pd.merge(df,df1,on='id',how="inner")


# In[36]:


pd.merge(df,df1,on='id',how="left")


# In[37]:


pd.merge(df,df1,on='id',how="right")


# In[38]:


pd.merge(df,df1,on='id',how="outer")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




