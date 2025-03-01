#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


height=[1,2,3,4,5]
weight=[10,20,30,40,50]
height=np.array(height)
weight=np.array(weight)


# In[4]:


height


# In[5]:


print(type(height))


# In[6]:


a = np.array([[1,0,1,0,2,3], [1,3,0,1,2,0], [0,1,0,0,1,3]])
b = a[:,1:3]
print(b)


# In[7]:


a = np.array([0, 1, 2])
b = np.array([5, 5, 5])
a + b
a + 5


# In[10]:


a=np.arange(10)
b=np.power(a,2)
print(b)
b.max()


# In[11]:


import pandas as pd


# In[12]:


number=range(1,100,5)
number


# In[13]:


pd.Series(number)


# In[15]:


data={"Name" : ["Abhay","Shubhangi","Shubhay"],
     "Dept": ["Computer","Electronics","Data Science"],
    "Roll Number" : [1,2,3]}

df=pd.DataFrame(data)
print(df)


# In[4]:


subject=pd.Series(['Engilsh','Maths','science'])
marks=pd.Series([50,70,55])
CGPA=pd.Series([2.5,3.5,2.7])
pd.DataFrame([subject,marks,CGPA], index=['Subject','Marks','CGPA']).T


# In[8]:


import pandas as pd


# In[12]:


data={"Name" : ["Abhay","Shubhangi","Shubhay"],
     "Dept": ["Computer","Electronics","Data Science"],
    "Roll Number" : [1,2,3]}
df=pd.DataFrame(data)
print(df)


# 

# In[14]:


df["marks"]=df["Roll Number"]*20
df


# In[15]:


df.shape


# In[20]:


df.iloc[[1,2]]


# In[ ]:




