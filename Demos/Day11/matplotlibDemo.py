#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pip install matplotlib


# In[2]:


import matplotlib.pyplot as pl


# In[ ]:





# In[ ]:





# In[ ]:





# In[3]:


l=["s1","s2","s3","s4","s5"]
l1=[45, 38, 56,77,80]

pl.plot(l,l1)
pl.title("test")
pl.show()


# In[ ]:





# In[ ]:





# In[5]:


l=["s1","s2","s3","s4","s5"]
l1=[45, 38, 56,77,80]

pl.plot(l,l1)
pl.title("Student data")
pl.xlabel("Student Names")
pl.ylabel("Marks")
pl.show()


# In[ ]:





# In[ ]:





# In[6]:


l=["s1","s2","s3","s4","s5"]
l1=[45, 38, 56,77,80]

pl.bar(l,l1)
pl.title("Student data")
pl.xlabel("Student Names")
pl.ylabel("Marks")
pl.show()




# In[9]:


l=["s1","s2","s3","s4","s5"]
l1=[45, 38, 56,77,80]

pl.barh(l,l1)
pl.title("Student data")
pl.xlabel("Student marks")
pl.ylabel("student names")
pl.show()


# In[10]:


l=["s1","s2","s3","s4","s5"]
l1=[45, 38, 56,77,80]

pl.barh(l,l1,color="red")
pl.title("Student data")
pl.xlabel("Student marks")
pl.ylabel("student names")
pl.show()


# In[12]:


l=["s1","s2","s3","s4","s5"]
l1=[45, 38, 56,77,80]

pl.scatter(l,l1)
pl.title("Student data")
pl.xlabel("Student Names")
pl.ylabel("Marks")
pl.show()


# In[18]:


l=["s1","s2","s3","s4","s5"]
l1=[45, 38, 56,77,80]

pl.plot(l,l1, marker="*")
pl.title("Student data")
pl.xlabel("Student Names")
pl.ylabel("Marks")
pl.show()


# In[21]:


l=["s1","s2","s3","s4","s5"]
l1=[45, 38, 56,77,80]

pl.plot(l,l1, marker="*",ls="-.")
pl.title("Student data")
pl.xlabel("Student Names")
pl.ylabel("Marks")
pl.show()


# In[22]:


l1=[45, 38, 56,77,80]

pl.hist(l1)
pl.show()


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





# In[14]:


get_ipython().run_line_magic('pinfo', 'mp.title')


# In[ ]:





# In[ ]:





# In[10]:


get_ipython().run_line_magic('pinfo', 'mp.bar')


# In[ ]:





# In[ ]:





# In[ ]:




