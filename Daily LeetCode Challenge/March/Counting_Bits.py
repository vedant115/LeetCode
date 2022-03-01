# LeetCode 338

"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Example 1:
Input: n = 2
Output: [0,1,1]

Explanation:
0 --> 0
1 --> 1
2 --> 10
"""

def countBits(self, n: int) -> List[int]:
    res = []
    for i in range(n+1):
        res.append(format(i, 'b').count('1'))
    return res
	
	
def countBits(self, n: int) -> List[int]:                
    res = [format(i, 'b').count('1') for i in range(n+1)]
    return res
