
# coding: utf-8

# # Promedio lista

# In[1]:


mis_valores = [5, 6, 10, 13, 3, 4]


# In[2]:


mis_valores


# In[4]:


a = sum(mis_valores)


# In[5]:


b = len (mis_valores)


# In[6]:


a/b


# # grupo con altura máxima

# In[10]:


grupo_1 = [177,145,167,190,140,150,180,130]

grupo_2 = [165,176,145,189,170,189,159,190]

grupo_3 =[145,136,178,200,123,145,145,134]

grupo_4 = [201,110,187,175,156,165,156,135]


# In[12]:


todos = [grupo_1, grupo_2,grupo_3,grupo_4]


# In[13]:


todos


# In[28]:


x_1 = max (grupo_1)
x_2 = max (grupo_2)
x_3 = max (grupo_3)
x_4 = max (grupo_4)


# In[30]:


max (x_1,x_2,x_3,x_4)


# In[34]:


def alturas(máximo):
 return {"grupo_1":x_1, "grupo_2":x_2, "grupo_3": x_3, "grupo_4": x_4}[máximo]


# In[38]:


Grupos = ["grupo_1", "grupo_2", "grupo_3", "grupo_4"]


# In[40]:


print (max (Grupos,key=alturas))

