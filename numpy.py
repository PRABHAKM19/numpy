#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[6]:


a=np.zeros(3)
a


# In[7]:


a.shape


# In[12]:


a.shape=(3,1)
a


# In[16]:


a=np.ones(3)
type(a[0])


# In[17]:


a=np.empty(3)
a


# In[19]:


a=np.linspace(2,10,5)
a


# In[21]:


a=np.array([10,5])
a


# In[22]:


type(a)


# In[30]:


z=[[1,2,6,3,9,6],[7,4,9,3,0,1,5]]
a=np.array(z)


# In[31]:


np.random.seed(0)
z=np.random.randint(10,size=6)
z


# In[33]:


z[0]


# In[34]:


z[0:4]


# In[35]:


z[-1]


# In[ ]:





# In[ ]:




