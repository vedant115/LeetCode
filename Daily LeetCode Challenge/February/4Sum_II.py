# LeetCode 454

'''
Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
'''

'''
Example 1:

Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
'''

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count1 = {}
        ans=0
        
        for a in nums1:
            for b in nums2:
                count1[a+b] = 1 + count1.get(a+b, 0)
                
        for c in nums3:
            for d in nums4:
                ans+=count1.get(-(c+d), 0)
                
        return ans

# Same approach short 

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count = Counter(a + b for a in nums1 for b in nums2)
        return sum(count[-c-d] for c in nums3 for d in nums4)
    
