# LeetCode 316. 

"""
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example 1:
Input: s = "bcabc"
Output: "abc"

Example 2:
Input: s = "cbacdcbc"
Output: "acdb"
"""

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] not in stack:
                while (stack and stack[-1] > s[i] and stack[-1] in s[i+1:]):
                    stack.pop()
                stack.append(s[i])

        return "".join(stack)
