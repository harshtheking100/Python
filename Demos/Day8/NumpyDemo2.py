#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


a= np.random.randint(1,13,(3,4))
print(a)


# In[4]:


a.resize(2,2)
print(a)


# In[7]:


a.resize(3,3)
a


# In[10]:


b=a.flatten()
print(b)


# In[11]:


print(a)


# In[12]:


a=a.reshape(-1)
print(a)


# In[13]:


a= np.arange(1,5).reshape(2,2)
print(a)


# In[14]:


a+2


# In[16]:


print(a)
a*3


# In[17]:


print(a)
a/3


# In[18]:


print(a)
a**3


# In[19]:


print(a)
a%3


# In[20]:


a= np.random.randint(1,9,(3,3))
b=np.random.randint(1,9,(3,3))
print(a)
print(b)


# In[21]:


a+b


# In[22]:


a-b


# In[23]:


b-a


# In[24]:


a*b


# In[25]:


a/b


# In[26]:


a%b


# In[27]:


a//b


# In[28]:


a= np.random.randint(1,9,(3,3))
print(a)


# In[29]:


print(a.sum())
print(a.min())
print(a.max())


# In[30]:


print(a)
print(a.sum(axis=0))
print(a.min(axis=0))
print(a.max(axis=0))


# In[31]:


print(a)
print(a.sum(axis=1))
print(a.min(axis=1))
print(a.max(axis=1))


# In[32]:


print(a)


# In[33]:


print(b)


# In[34]:


#transpose of matrix
a.T


# In[36]:


#matrics Multiplication
a.dot(b)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




