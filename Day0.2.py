#!/usr/bin/env python
# coding: utf-8

# Move Zeroes

# In[77]:


from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]):
        j=0
        n = len(nums)
        for num in nums:
            if(num != 0):
                nums[j] = num
                j += 1
        for x in range (j, n):
            nums[x] = 0
            print(nums)
            
s = Solution()
k = s.moveZeroes([2,9,0,5,3,2])


# Boats to Save People

# In[1]:


from typing import List
class Solution:
    def numRescueBoats(self,people:List[int],limit:int)->None:
        people.sort()
        start=0
        end=len(people)-1
        boat = 0
        while start <= end:
            if (people[start] + people[end] <= limit):
                start += 1
            end -= 1
            boat += 1
        return boat
    
s=Solution()
a = s.numRescueBoats([3,2,2,1],3)
print(a)

