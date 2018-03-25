
# coding: utf-8

# In[58]:


import numpy as np


# In[17]:


def f(x):
    return x**2


# In[18]:


def f_2(x):
    return x**3


# In[19]:


def f_3(x):
    return ((x**3)+5*x)


# In[20]:


def d_f(x):
    return 2*x


# In[21]:


def d_f2(x):
    return 3*x**2 


# In[22]:


def d_f3(x):
    return ((3*x**2)+5)


# In[38]:


def vector_sum(x,y):
    return np.add(x,y)


# In[24]:


def vector_less(x,y):
    return np.subtract(x,y)


# In[132]:


def vector_magnitude(x):
    y=((sum(i**2 for i in x))**.5)
    return (int(y))


# In[92]:


def vec5():
    return np.ones((5),dtype=int)


# In[37]:


def vec3():
    return np.zeros((3)).astype(int)
vec3()


# In[28]:


def vec2_1():
    return np.array([1,0])


# In[29]:


def vec2_2():
    return np.array([0,1])


# In[129]:


def matrix_multiply(vec,matrix):
    return ((np.dot(vec,matrix)))


# In[130]:


matrix_multiply([4,3],[[3,0],[0,2]])


# In[131]:


np.array_equal([12,6],matrix_multiply([4,3],[[3,0],[0,2]]))

