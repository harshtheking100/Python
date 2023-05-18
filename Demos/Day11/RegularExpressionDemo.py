#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re


# In[3]:


s="quick brown fox jumps over the lazy dog."


# In[4]:


re.match("^quick",s)


# In[5]:


re.match("^fox",s) # no answer


# In[7]:


re.search("dog.$",s)


# In[8]:


re.search("l..y",s)


# In[9]:


s="quick brown fox jumps over the lazy crazy buzy laay dog."
re.search("l..y",s)


# In[10]:


s="quick brown fox jumps over the lazy crazy buzy laay dog."
re.findall("l..y",s)


# In[15]:


s="quick brown fox jumps over the lazy crazy buzy laay dog."
re.findall("..zy",s)


# In[16]:


s="quick brown fox jumps over the lazy crazy buzy laay dog."
list(re.finditer("..zy",s))


# In[17]:


s="quick brown fox 111 over 22 555 the lazy crazy buzy 666 laay 123 dog."
list(re.finditer("\d",s))


# In[18]:


s="quick brown fox 111 over 22 555 the lazy crazy buzy 666 laay 123 dog."
list(re.finditer("\d{3}",s))


# In[19]:


s="quick brown fox 111 over 22 555 the lazy crazy_buzy 666 laay 123 dog_cat."
list(re.finditer("[a-z]_[a-z]",s))


# In[20]:


s="quick brown fox 111 over 22 555 the lazy crazy_buzy 666 laay 123 dog_cat."
list(re.finditer("[a-z]*_[a-z]",s))


# In[21]:


s="quick brown fox 111 over 22 555 the lazy crazy_buzy 666 laay 123 dog_cat."
list(re.finditer("[a-z]*_[a-z]*",s))


# In[23]:


s="quick brown fox 111 over 123-345-678 the lazy crazy_buzy 666 laay 123 dog_cat.123-345-678 hkhk kjkjkl kjklkj 123-345-678"
list(re.finditer("\d{3}-\d{3}-\d{3}",s))


# In[24]:


s="i am happy and cool"
list(re.finditer("[a-z]{2}",s))


# In[25]:


s="i am happy and cool"
list(re.finditer("[p]{2}",s))


# In[29]:


s="i am happy and cool, coppy ....mappy"
list(re.finditer("[a-z]+[p]{2}[a-z]+",s))


# In[30]:


s="i am happy and cool, coppy ....mappy"
re.split(" ",s)


# In[33]:


s="i am happy and cool, coppy ....mappy"
re.split(".. ",s) #splits on two char and space


# In[34]:


s="i am happy and cool, coppy ....mappy"
re.sub("am","AM",s) #replace


# In[35]:


s="1 2 3 4 5 6 11 22 33 56 78 90 123 456 789 234 678"
list(re.finditer("[0-9][0-9]",s))


# In[37]:


s="1 2 3 4 5 6 11 22 33 56 78 90 123 456 789 234 678"
list(re.finditer("([0-9][0-9])\s{1}",s))


# In[42]:


p="[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}"
pattern = re.compile(p)
s="Email addresses can be on servers on a subdomain as in john@server.com  All of the above regexes match this email address, because I included a dot in the character class after the @ symbol. But the above regexes also match john@aol...com which is not valid due to the consecutive dots."
re.findall(pattern,s)


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




