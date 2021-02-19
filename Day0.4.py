#!/usr/bin/env python
# coding: utf-8

#  Median of two Sorted Array (not solved)

# In[42]:


from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         num1.sort()
#         num2.sort()
        i = num1 + num2
        i.sort()
        for n in range(len(i)):
            print(n)
s = Solution
nums1 = [4,6]
nums2 = [3,5]
# a = s.findMedianSortedArrays(nums1,nums2)
print(i)


# In[21]:


num = [4,6,3,5,2,7,9,2]
def ok():
    num.sort()
    for i in range(len(num)):
        print (i)
        i+= 1
ok()


# In[ ]:


def cal():
    num = int(input("Enter your Number: "))
    if num >= 0:
        if num == 0:
            return "num equal to 0"
        elif num > 0:
            return "num greater than 0"
    else:
        return "num less than 0"
            
for x in range(0,3):
    print(cal())


# Container with Most Water

# In[ ]:


from typing import List
class Solution:
    def maxArea(self, height:List[int])-> int:
        maxarea = 0
        start  = 0
        end = len(height) - 1
        
        while (start < end):
            maxarea = max(maxarea,min(height[start],height[end])*(end-start))
            if (height[start]<height[end]):
                start += 1
            else:
                end -= 1
        return maxarea
    
# myheight = 
s = Solution()
answer = s.maxArea([1,8,6,2,5,4,8,3,7])
print(answer)


# In[24]:


number = [4,9,5,2,3,7,4,2,9,8,5,7,5,7]
for i in number:
    number.sort()
    print(i)
    


# In[25]:


counter = 0
while counter < 3:
    print ("on loop")
    counter += 1
else:
    print("exit loop")


# In[26]:


for val in "string":
    if val == "i":
        break
    print(val)
        


# In[30]:


for val in "string":
    if val == "i":
        continue
    print(val)
        

