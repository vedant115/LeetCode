# LeetCode 347. 

"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
"""

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for n in nums:
            counter[n] = counter.get(n, 0) + 1
            
        return sorted(counter , key = lambda ki: counter[ki], reverse=True)[:k]
			
# ------------------------------------------------------------------------------------ #

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [n[0] for n in Counter(nums).most_common(k)]
