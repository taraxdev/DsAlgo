#!/usr/bin/env python
# coding: utf-8

# Two Sum

# In[32]:


from typing import List
class Solution:
    def sumall(arr:List[int],n:int,target:int):
        n = len(arr)
        for i in range(0,n):
            for j in range(i+1,n):
                sum = arr[i] + arr[j]
                if sum == target:
                    return [i,j]
                    
                    
                    
arr = [1, 5, 7, -1, 5]

sum = 6
s=Solution
s.sumall(arr, n, sum)


# Binary Search

# In[73]:



def binary(list,item):
    start = 0
    end = len(list) - 1
    list.sort()
    while start <= end:
        mid = (start+end)
        target = list[mid]
        if target == item:
            return mid
        if target > item:
            end = mid - 1
        else:
            start = mid + 1
    return None

mylist = [8,7,43,8,32,1,89,14]
print (binary(mylist,32))


# In[24]:


horsemen = ["war", "famine", "pestilence", "death"]
i = 0
num = len(horsemen)
while i < num:
    print (horsemen[i])
    i += 1
    

