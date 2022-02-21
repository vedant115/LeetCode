# LeetCode 169

'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''

def majorityElement(self, nums: List[int]) -> int:
    c = dict(Counter(nums))
    c = sorted(c.keys(), key = lambda i: c[i])
    return (c[-1])
  
  
def majorityElement(self, nums: List[int]) -> int:
    return collections.Counter(nums).most_common()[0][0]
  
  
def majorityElement(self, nums: List[int]) -> int:
		t=len(nums)//2

		for i in set(nums):
			if nums.count(i)>t:
				return i
      
      
def majorityElement(self, nums: List[int]) -> int:
    # median (by definition of majority value) has to be the majority value.
    mid = len(nums)//2
    return sorted(nums)[mid]
  
