# Leetcode 410. 

"""
Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these m subarrays.

Example 1:
Input: nums = [7,2,5,10,8], m = 2
Output: 18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
"""

def splitArray(self, nums: List[int], m: int) -> int:
    lo, hi = max(nums), sum(nums)
    while lo < hi:
        mid = (lo+hi)//2
        tot, cnt = 0, 1
        for num in nums:
            if tot+num<=mid: 
                tot += num
            else:
                tot = num
                cnt += 1
        if cnt>m: lo = mid+1
        else: hi = mid
    return hi
