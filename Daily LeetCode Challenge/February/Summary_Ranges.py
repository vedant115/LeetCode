# LeetCode 228.

"""
You are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
 
Example 1:
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]

Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
"""

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        start, cur, end = nums[0], nums[0], None
        output = []
        
        for n in nums[1:]:
            cur += 1
            if n == cur:
                end = n
            else:
                if not end:
                    output.append(str(start))
                else:
                    output.append(str(start)+"->"+str(end))
                start = n
                cur = n
                end = None
                
        if not end:
            output.append(str(start))
        else:
            output.append(str(start)+"->"+str(end))
            
        return output
      
