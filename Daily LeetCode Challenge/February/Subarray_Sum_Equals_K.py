# LeetCode 560

"""
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
"""

def subarraySum(self, nums: List[int], k: int) -> int:
	ans=0
	prefsum=0
	d={0:1}
  
	for num in nums:
		prefsum = prefsum + num
		if prefsum-k in d:
			ans = ans + d[prefsum-k]
      
		if prefsum not in d:
			d[prefsum] = 1
		else:
			d[prefsum] = d[prefsum]+1
      
	return ans
  
