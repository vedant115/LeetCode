# LeetCode 344

"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
"""

def reverseString(self, s: List[str]) -> None:
    i = 0
    j = len(s)-1
    
    while(i<j):
        s[i], s[j] = s[j], s[i]
        i+=1
        j-=1

#-------------------------------------------------#

def reverseString(self, s: List[str]) -> None:
    stack = []
    for c in s:
        stack.append(c)
    i = 0
    while stack:
        s[i] = stack.pop()
        i+=1
#-------------------------------------------------#
						
def reverseString(self, s: List[str]) -> None:
    def reverse(l, r):
        if l < r:
            s[l], s[r] = s[r], s[l]
            reverse(l+1, r-1)
            
    reverse(0, len(s)-1)
		
