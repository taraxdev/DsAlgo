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


# ## Maximuma & Minimum of an array using minimum number of Comparisons

# ##### naive solution

# In[27]:


def findMinAndMax(A):
    max = min = A[0]
    for i in range(1,len(A)):
        if A[i] > max:
            max = A[i]
            
        if A[i] < min:
            min = A[i]
            
    print("Max: ",max)
    print("Min: ",min)
    
A = [3,8,5,9,2,34,45,44,]

findMinAndMax(A)


# ##### compare in pairs

# In[33]:


def findMinAndMax(arr):
    n = len(arr)
    
    if (n%2 == 0):
        mx = max(arr[0], arr[1])
        mn = min(arr[0], arr[1])
        i = 2
    else:
        mx = mn = arr[0]
        i=1
        
    while(i<n-1):
        if arr[i]<arr[i+1]:
            mx = max(mx,arr[i+1])
            mn = min(mx,arr[i])
        else:
            mx = max(mx,arr[i])
            mn = min(mn,arr[i+1])    
        i += 2
    return (mx,mn)

arr = [23,45,243,435,45,643,3]
findMinAndMax(arr)


# In[ ]:





# In[ ]:





# In[ ]:




