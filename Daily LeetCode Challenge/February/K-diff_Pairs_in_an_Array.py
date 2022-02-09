# LeetCode 532

"""
Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

0 <= i < j < nums.length
|nums[i] - nums[j]| == k
Notice that |val| denotes the absolute value of val.
"""
 
"""
Example 1:

Input: nums = [3,1,4,1,5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.
"""


def findPairs(self, nums: List[int], k: int) -> int:
    cnt=0
    c=Counter(nums)
    
    if k==0:
        for key,v in c.items():
            if v>1:
                cnt+=1
    else:
        for key,v in c.items():
            if key+k in c:
                cnt+=1
    return cnt
    
