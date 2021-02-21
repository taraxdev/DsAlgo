#!/usr/bin/env python
# coding: utf-8

# Majority Elements

# In[38]:


def majorityElement(arr,size):
    map = {}
    for i in range(size):
        if arr[i] in map:
            map[arr[i]] += 1
        else:
            map[arr[i]] = 1
    count = 0
    for key in map:
        if map[key] > size / 2:
#             count = 1
            print("majority found : ",key)
#             break
    if count == 0:
        print ("no majority found")
        
arr = [2, 2, 2, 2, 5, 5, 2, 3, 3] 
n = len(arr)

majorityElement(arr,n)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




