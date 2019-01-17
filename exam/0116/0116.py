
# coding: utf-8

# In[5]:


import random

prob = 0.1
total = bomb = 0
iter_count = 100000000

for i in range(iter_count):
    total += 1
    if random.random() <= prob:
        bomb += 1
        prob = 0.1
    else:
        prob += 0.01
        
print(bomb / total)

