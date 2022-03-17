# LeetCode 856. 

"""
Given a balanced parentheses string s, return the score of the string.

The score of a balanced parentheses string is based on the following rule:

"()" has score 1.
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.
 

Examples

Input: s = "()"
Output: 1

Input: s = "(()(()))"
Output: 6

"""

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [] 
        
        for i in s:
            if i == "(":
                stack.append(0)
            else:
                val = 0
                while stack[-1] != 0:
                    val += stack.pop()
                val = max(2*val, 1)
                stack.pop()
                stack.append(val)
                
        return sum(stack)
			
