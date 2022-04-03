# LeetCode 31. 

"""
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are considered permutations of arr: [1,2,3], [1,3,2], [3,1,2], [2,3,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]
"""

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        L = len(nums)
        for i in reversed(range(L - 1)):
            # Search
            cand = -1
            for j in range(i + 1, L):
                if nums[j] > nums[i]:
                    if cand < 0 or nums[j] < nums[cand]: cand = j
            if cand < 0: continue

            # Swap
            nums[i], nums[cand] = nums[cand], nums[i]
                        
            # Insertion sort
            j = i + 2
            while j < L:
                k = j
                while k - 1 > i and nums[k - 1] > nums[k]:
                    nums[k - 1], nums[k] = nums[k], nums[k - 1]
                    k -= 1
                j += 1

            break
        else:
            nums.reverse()
						
