#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pip install pillow 


# In[6]:


from PIL import Image


# In[8]:


img =Image.open(r"C:\Users\Shruti\Downloads\images\image2.jpeg")


# In[9]:


img.show()


# In[10]:


display(img)


# In[11]:


img.mode #image mode


# In[12]:


img.filename #name of file with path


# In[13]:


img.format #type of image


# In[14]:


img.size


# #methods
# rotate()
# resize()
# reduce()
# thumbnail()
# save()
# convert()

# In[15]:


img.rotate(45) #provide angle of rotation


# In[16]:


img.rotate(90)


# In[18]:


img2=img.rotate(180)
img2.save(r"C:\Users\Shruti\Downloads\images\test1.png")
display(img2)


# In[23]:


img2=img.reduce((10,10))


# In[24]:


img2.size


# In[26]:


img.resize((300,300))


# In[27]:


img.thumbnail((10,10))


# In[28]:


img


# In[29]:


img2


# In[30]:


img =Image.open(r"C:\Users\Shruti\Downloads\images\img1.jpeg")


# In[31]:


img


# In[32]:


img.convert("L")


# In[33]:


img.width


# In[34]:


img.height


# In[36]:


img.info


# In[ ]:





# In[ ]:





# In[ ]:





# In[21]:





# In[22]:


img.size


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




