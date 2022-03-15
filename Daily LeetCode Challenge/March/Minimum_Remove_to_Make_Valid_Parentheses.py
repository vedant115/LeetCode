# LeetCode 1249. 

"""
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"

Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
"""


 def minRemoveToMakeValid(self, s: str) -> str:
     stack = []
     S = list(s)
     N = len(s)
     
     for i in range(N):
         if S[i] == "(":
             stack.append(i)
         elif S[i] == ")":
             if stack:
                 stack.pop()
             else:
                 S[i] = ""
                 
     for j in stack:
         S[j] = ""
         
     return "".join(S)
			

def minRemoveToMakeValid(self, s: str) -> str:
    cnt_open, cnt_close, res = 0, 0, ''
    for ch in s:
        if ch == '(': cnt_open += 1
        if ch == ')': cnt_close += 1
        if cnt_open < cnt_close:
            cnt_close -= 1
        else:
            res = res + ch
				
    s = res
    
    cnt_open, cnt_close, res = 0, 0, ''
    for ch in reversed(s):
        if ch == '(': cnt_open += 1
        if ch == ')': cnt_close += 1
        if cnt_close < cnt_open:
            cnt_open -= 1
        else:
            res = ch + res
            
    return res
            
