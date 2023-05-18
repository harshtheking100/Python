#!/usr/bin/env python
# coding: utf-8

# In[3]:


a=10
print(a)
b=100
print(b)


# In[5]:


import numpy as np
print(np.__version__)


# In[6]:


lst=[1,2,3,4,5]
a=np.array(lst)
print(a)


# In[7]:


print(type(a))
print(a.ndim)
print(a.size)
print(a.shape)
print(a.itemsize)
print(a.dtype)
print(a.data)
print(list(a.data))


# In[8]:


lst=[[1,2,3,4,5],[10,20,30,40,50]]
a=np.array(lst)
print(a)


# In[10]:


print(type(a))
print(a.ndim)
print(a.size)
print(a.shape)
print(a.itemsize)
print(a.dtype)
print(a.data)


# In[11]:


lst=[[[1,2,3,4,5],[10,20,30,40,50]],[[11,21,31,41,51],[110,120,130,140,150]]]
a=np.array(lst)
print(a)


# In[12]:


print(type(a))
print(a.ndim)
print(a.size)
print(a.shape)
print(a.itemsize)
print(a.dtype)
print(a.data)


# In[14]:


#Array Creation Methods
#1. array
#2. ones
#3. zeros
#4. empty
#5.full
#6.identity
#7. eye
#8.random
#9. random.randint
#10 arange

#Reshape
#resize
#flattern


# In[15]:


#1
lst=(1,2,3,4,5)
a=np.array(lst)
print(a)


# In[16]:


lst=(1,2,3,4,5)
a=np.array(lst,dtype=float)
print(a)


# In[17]:


lst=(1,2,3,4,5)
a=np.array(lst,dtype=complex)
print(a)


# In[19]:


#2
a= np.ones(5)
print(a)
print(type(a))
print(a.ndim)
print(a.size)
print(a.shape)
print(a.itemsize)
print(a.dtype)
print(a.data)


# In[20]:


a= np.ones(5,dtype=int)
print(a)
print(type(a))
print(a.ndim)
print(a.size)
print(a.shape)
print(a.itemsize)
print(a.dtype)
print(a.data)


# In[21]:


a= np.ones((5,4),dtype=int)
print(a)
print(type(a))
print(a.ndim)
print(a.size)
print(a.shape)
print(a.itemsize)
print(a.dtype)
print(a.data)


# In[22]:


a= np.ones((2,5,4),dtype=int)
print(a)
print(type(a))
print(a.ndim)
print(a.size)
print(a.shape)
print(a.itemsize)
print(a.dtype)
print(a.data)


# In[23]:


a= np.zeros(3,dtype=int)
print(a)
print(type(a))
print(a.ndim)
print(a.size)
print(a.shape)
print(a.itemsize)
print(a.dtype)
print(a.data)


# In[24]:


a= np.zeros((2,5,4),dtype=int)
print(a)
print(type(a))
print(a.ndim)
print(a.size)
print(a.shape)
print(a.itemsize)
print(a.dtype)
print(a.data)


# In[25]:


a= np.empty((2,5,4),dtype=int)
print(a)
print(type(a))
print(a.ndim)
print(a.size)
print(a.shape)
print(a.itemsize)
print(a.dtype)
print(a.data)


# In[26]:


a= np.identity(5,dtype=int)
print(a)
print(type(a))
print(a.ndim)
print(a.size)
print(a.shape)
print(a.itemsize)
print(a.dtype)
print(a.data)


# In[27]:


a= np.eye(5,4,k=0,dtype=int)
print(a)
print(type(a))
print(a.ndim)
print(a.size)
print(a.shape)
print(a.itemsize)
print(a.dtype)
print(a.data)


# In[28]:


a= np.eye(5,4,k=1,dtype=int)
print(a)


# In[29]:


a= np.eye(5,4,k=-1,dtype=int)
print(a)


# In[30]:


a= np.full(5,4,dtype=int)
print(a)


# In[31]:


a= np.full((5,6),4,dtype=int)
print(a)


# In[33]:


a= np.full((5,2,3),8,dtype=int)
print(a)


# In[34]:


a= np.random.random(5)
print(a)


# In[35]:


a= np.random.random((5,3))
print(a)


# In[37]:


a= np.random.randint(1,10,5)
print(a)


# In[38]:


a= np.random.randint(1,10,(2,5))
print(a)


# In[39]:


a= np.random.randint(1,20,(2,5,6))
print(a)


# In[40]:


a= np.arange(1,10)
print(a)


# In[41]:


a= np.arange(11,100)
print(a)


# In[42]:


a= np.arange(1,100,2)
print(a)


# In[43]:


a= np.arange(1,10).reshape(3,3)
print(a)


# In[44]:


a= np.arange(1,13).reshape(3,2,2)
print(a)


# In[45]:


#Error
a= np.arange(1,10).reshape(3,3,2)
print(a)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




