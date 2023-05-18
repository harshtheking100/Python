#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[4]:


d={"name":["radha","keshav","ovi"],"age":[10,20,30],"marks":[56.34,90.56,78.38]}
df=pd.DataFrame(d)
print(df)


# In[6]:


arr=np.arange(1,5)
df1=pd.DataFrame(arr,index=['a','b','c','d'],columns=["Test"])
print(df1)


# In[8]:


import pandas as pd
dt={'id': {0: 1,1: 2,2: 3,3: 4,4: 5,5: 6,6: 7,7: 8,8: 9,9: 10,10: 11,11: 12,
  12: 13,13: 14,14: 15,15: 16,16: 17,17: 18,18: 19,19: 20,20: 21,21: 22,
  22: 23,23: 24,24: 25,25: 26,26: 27,27: 28,28: 29,29: 30,30: 31,31: 32,32: 33,
  33: 34,34: 35},
 'name': {0: 'John Deo',1: 'Max Ruin',2: 'Arnold',3: 'Krish Star',4: 'John Mike',
  5: 'Alex John',6: 'My John Rob',7: 'Asruid',8: 'Tes Qry',9: 'Big John',
  10: 'Ronald',11: 'Recky',12: 'Kty',13: 'Bigy',14: 'Tade Row',15: 'Gimmy',
  16: 'Tumyu',17: 'Honny',18: 'Tinny',19: 'Jackly',20: 'Babby John',21: 'Reggid',
  22: 'Herod',23: 'Tiddy Now',24: 'Giff Tow',25: 'Crelea',26: 'Big Nose',
  27: 'Rojj Base',28: 'Tess Played',29: 'Reppy Red',30: 'Marry Toeey',
  31: 'Binn Rott',32: 'Kenn Rein',33: 'Gain Toe',34: 'Rows Noump'},
  'class': {0: 'Four', 1: 'Three',2: 'Three',3: 'Four',4: 'Four', 5: 'Four',
  6: 'Five',7: 'Five',8: 'Six',9: 'Four',10: 'Six',11: 'Six',12: 'Seven',
  13: 'Seven',14: 'Four',15: 'Four',16: 'Six',17: 'Five',18: 'Nine',19: 'Nine',
  20: 'Four',21: 'Seven',22: 'Eight',23: 'Seven',24: 'Seven',25: 'Seven',
  26: 'Three',27: 'Seven',28: 'Seven',29: 'Six',30: 'Four',31: 'Seven',32: 'Six',
  33: 'Seven',34: 'Six'},'mark': {0: 75,1: 85,2: 55,3: 60,4: 60,5: 55,6: 78,
  7: 85,8: 78,9: 55,10: 89,11: 94,12: 88,13: 88,14: 88,15: 88,16: 54,17: 75,
  18: 18,19: 65,20: 69,21: 55,22: 79,23: 78,24: 88,25: 79,26: 81,27: 86,28: 55,
  29: 79,30: 88,31: 90,32: 96,33: 69,34: 88},
 'gender': {0: 'female',1: 'male',2: 'male',3: 'female',4: 'female',5: 'male',
  6: 'male',7: 'male',8: 'male',9: 'female',10: 'female',11: 'female',12: 'female',
  13: 'female',14: 'male',15: 'male',16: 'male',17: 'male',18: 'male',19: 'female',
  20: 'female',21: 'female',22: 'male',23: 'male',24: 'male',25: 'male',26: 'female',
  27: 'female',28: 'male',29: 'female',30: 'male',31: 'female',32: 'female',
  33: 'male',34: 'female'}}
df=pd.DataFrame(data=dt)
print(df)


# In[9]:


df.info()


# In[10]:


df.describe()


# In[11]:


df.head()


# In[12]:


df.head(7)


# In[13]:


df.tail()


# In[14]:


df.tail(4)


# In[15]:


df.shape


# In[16]:


df.shape[0] #rows


# In[17]:


df.shape[1] #col


# In[18]:


df.columns


# In[19]:


df.index


# In[20]:


df["name"]


# In[21]:


df[["id","name","class"]]


# In[22]:


df[df["mark"]>70]


# In[23]:


df[(df["mark"]>70) & (df["gender"]=="male")]


# In[27]:


df[(df["mark"]>80) & (df["class"]=="Five")]


# In[28]:


df[(df["mark"]>80) | (df["class"]=="Five")]


# In[30]:


df[(df["mark"]>60) & (df["class"]=="Six") & (df["gender"]=="female")]


# In[31]:


df["mark"]


# In[32]:


df["mark"].value_counts()


# In[33]:


df["gender"].value_counts()


# In[34]:


df.sort_values("mark")


# In[35]:


df.sort_values("mark",ascending=False)


# In[36]:


df.sort_values(["mark","name"])


# In[37]:


df.sort_values(["mark","name"],ascending=[True,False])


# In[38]:


g=df.groupby("mark")


# In[39]:


g.groups


# In[40]:


g.get_group(88)


# In[41]:


g.first()


# In[42]:


g.count()


# In[43]:


g.last()


# In[44]:


g.size()


# In[45]:


dir(pd)


# In[46]:


df.min()


# In[47]:


df.max()


# In[48]:


df.count()


# In[49]:


df.sum()


# In[50]:


df["id"].sum()


# In[53]:


print(df["mark"].sum())
print(df["mark"].min())
print(df["mark"].max())
print(df["mark"].count())
print(df["mark"].mean())


# In[54]:


df.describe()


# In[55]:


df.apply(np.max)


# In[56]:


df.apply(np.min)


# In[57]:


df.loc[:,:]


# In[59]:


df.loc[0:4,:]


# In[60]:


df.loc[0:4,"class"]


# In[61]:


df.loc[0:4,["class","name"]]


# In[62]:


df.loc[0:4,"class":"gender"]


# In[63]:


df.loc[0::2,"class":"gender"]


# In[64]:


df.iloc[:,:]


# In[65]:


df.iloc[3:,1:3]


# In[66]:


df.iloc[::2,::2]


# In[67]:


df.iloc[::2,2]


# In[68]:


df


# In[69]:


df["total"]=10


# In[79]:


df["total"]=df["mark"]+5


# In[ ]:





# In[76]:


df


# In[73]:


df.pop("total") #delete #delete total from df


# In[78]:


df.drop(columns="total")#delete total from df


# In[83]:


df1=df.drop("total",axis=1) #delete total from df
df1


# In[85]:


df.drop("total",axis=1,inplace=True)
df


# In[87]:


df.drop(34,axis=0,inplace=True) #delete Row
df


# In[88]:


df.iloc[1,3]


# In[89]:


df.iloc[1,3]=90 #update marks to 90


# In[90]:


df


# In[93]:


df.loc[34]=[35,"Rupak","Ten",89 ,"Male"] #insert record in df
df


# In[94]:


df.loc[34]=[35,"Rupak1","Ten",89 ,"Male"] #update record in df
df


# In[98]:


df.to_csv(r"E:\Python_local\data\studentdata.csv",index=False)


# In[99]:


df1=pd.read_excel(r"E:\Python_local\data\Order_data.xlsx")
df1


# In[101]:


df1["Unit Cost"].dtype


# In[103]:


df1.corr()


# In[ ]:





# In[105]:


df2=df1["Unit Cost"].astype(int)
df2


# In[106]:


d={'a':[1,2,3],'b':[10,20,30]}
d1={'a':[11,21,31],'b':[110,210,310]}
df1=pd.DataFrame(d)
df2=pd.DataFrame(d1)
print(df1)
print(df2)


# In[119]:


pd.concat([df1,df2])


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





# In[82]:


df


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




