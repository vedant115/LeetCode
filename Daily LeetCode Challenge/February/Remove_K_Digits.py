# LeetCode 402

'''
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

Example 1:
Input: num = "1432219", k = 3
Output: "1219"

Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
'''

def removeKdigits(self, num: str, k: int) -> str:
    stack=[]
    
    for digit in num:
        # check if new digit is less than prev digit and removing prev digit.
        while stack and stack[-1] > digit and k:
            stack.pop()
            k-=1
        stack.append(digit)
    
    # if k has some value or there are all incresing elements so to remove last remaining k digits.
    if k:
        stack = stack[0:-k]
        
    ans = "".join(stack).lstrip("0")
    
    # if ans empty string return "0"
    return "0" if ans == "" else ans
  
