# LeetCode 136

'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:

Input: nums = [2,2,1]
Output: 1
'''

# I
def singleNumber(self, nums: List[int]) -> int:
    '''
    Counter =
    c={}
		for i in nums:
			if i not in c:
				c[i]=1
			else:
				c[i]=c[i]+1
    '''
    c = Counter(nums)
    for i in c:
        if c[i] == 1:
            return i
          
# II
def singleNumber(self, nums: List[int]) -> int:
    c = dict(Counter(nums))
    c = sorted(c.items(), key = lambda kv:(kv[1], kv[0]))
    return c[0][0]
  
# III
def singleNumber(self, nums: List[int]) -> int:
		result = 0

		for i in nums:
			result = result ^ i
		return result 
  
# OR
def singleNumber(self, nums: List[int]) -> int:
	  return reduce(lambda result, i: result ^ i, nums)
  
