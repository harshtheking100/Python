#!/usr/bin/env python
# coding: utf-8

# In[1]:


#install seaborn  #pip install seaborn


# In[2]:


import seaborn as sn


# In[3]:


sn.get_dataset_names() #list of data sets


# In[4]:


f=sn.load_dataset("fmri")


# In[5]:


f


# In[6]:


f.head(30)


# In[7]:


f.tail(23)


# In[8]:


f.columns


# In[10]:


sn.set(style="white")
sn.lineplot(x="subject",y="timepoint",data=f)


# In[11]:


sn.set(style="white")
sn.scatterplot(x="subject",y="timepoint",data=f)


# In[12]:


df=sn.load_dataset("iris")
df.columns


# In[13]:


sn.set(style="white")
sn.scatterplot(x="sepal_length",y="sepal_width",data=df)


# In[15]:


sn.set(style="white")
sn.lineplot(x="sepal_length",y="sepal_width",data=df)


# In[16]:


sn.set(style="white")
sn.lineplot(x="sepal_length",y="sepal_width",data=df,hue="species")


# In[17]:


sn.set(style="dark")
sn.lineplot(x="sepal_length",y="sepal_width",data=df,hue="species")


# In[18]:


sn.set(style="whitegrid")
sn.lineplot(x="sepal_length",y="sepal_width",data=df,hue="species")


# In[23]:


sn.set(style="ticks") #white, dark, whitegrid, darkgrid, ticks
sn.lineplot(x="sepal_length",y="sepal_width",data=df,hue="species")


# In[24]:


sn.set(style="ticks") #white, dark, whitegrid, darkgrid, ticks
sn.scatterplot(x="sepal_length",y="sepal_width",data=df,hue="species")


# In[25]:


cs=sn.color_palette()
sn.palplot(cs)


# In[26]:


sn.set(style="ticks") #white, dark, whitegrid, darkgrid, ticks
sn.lmplot(x="sepal_length",y="sepal_width",data=df,hue="species")


# In[27]:


sn.set(style="ticks") #white, dark, whitegrid, darkgrid, ticks
sn.relplot(x="sepal_length",y="sepal_width",data=df,hue="species")


# In[29]:


sn.set(style="ticks") #white, dark, whitegrid, darkgrid, ticks
sn.relplot(x="sepal_length",y="sepal_width",data=df,hue="species")


# In[39]:


sn.set(style="ticks") #white, dark, whitegrid, darkgrid, ticks
sn.displot(df, kde="True")


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





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




