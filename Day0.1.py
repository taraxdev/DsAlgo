#!/usr/bin/env python
# coding: utf-8

# ## Reverse an Array

# In[8]:


def reverse(A,start,end):
    while start < end:
        A[start],A[end] = A[end],A[start]
        start += 1
        end -= 1
        
A = [1,2,3,4,5]
s = reverse(A,0,4)
print(A)

