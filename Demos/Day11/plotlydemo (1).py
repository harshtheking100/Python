#!/usr/bin/env python
# coding: utf-8

# In[3]:


import plotly.graph_objects as go
import numpy as np


# In[ ]:





# In[11]:


xdata= np.random.randint(1,30,50)
ydata= np.random.randint(1,30,50)

fig=go.Figure(data=go.Scatter(x=xdata,y=ydata,mode="markers"))
fig


# In[14]:


xdata= ["india","pakistan","Mexiko","UK","USA"]
ydata= [1000,2345,6795,1234,900]

fig=go.Figure(data=go.Pie(labels=xdata,values=ydata))
fig


# In[15]:


xdata= ["india","pakistan","Mexiko","UK","USA"]
ydata= [1000,2345,6795,1234,900]

fig=go.Figure(data=go.Bar(x=xdata,y=ydata))
fig


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




