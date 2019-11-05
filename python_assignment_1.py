#!/usr/bin/env python
# coding: utf-8

# In[1]:


string = """
Twinkle, twinkle , little star,
    How I wondar what you are!
        Up above the world so high,
        Like a diamond in the sky.
Twinkle, twinkle , little star,
    How I wondar what you are!
"""

print(string)


# In[2]:


import sys
print(sys.version)


# In[6]:


from datetime import datetime
now = datetime.now()
print(f'Current Date and time: {now}')


# In[7]:


import math
circRadius = int(input('Enter circal Radius: '))
circArea = math.pi * (circRadius**2)
print(circArea)


# In[9]:


f_name = input('Enter first name: ')
l_name = input('Enter last name: ')
print(f'You name is {f_name[::-1]} {l_name[::-1]}')


# In[10]:


num_1 = int(input('Enter 1st number :'))
num_2 = int(input('Enter 2nd number :'))
print(f'Your Answer is : {num_1 + num_2}')


# In[ ]:




