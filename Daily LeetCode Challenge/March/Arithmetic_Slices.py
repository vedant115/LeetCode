# LeetCode 413. 

"""
An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
Given an integer array nums, return the number of arithmetic subarrays of nums.

A subarray is a contiguous subsequence of the array.


Example 1:
Input: nums = [1,2,3,4]
Output: 3

Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.
"""

def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
    N = len(nums)
    dp = [None]*(N-1)
    ans = 0
    
    for i in range(1, N):
        dp[i-1] = nums[i] - nums[i-1]
    
    m = 1
    
    for i in range(1, len(dp)):
        if dp[i] == dp[i-1]:
            ans += m
            m += 1
        else:
            m = 1
            
    return ans
	
