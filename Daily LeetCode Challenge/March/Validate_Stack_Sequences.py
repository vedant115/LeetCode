# LeetCode 946. 

"""
Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.

Example 1:
Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true

Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4),
pop() -> 4,
push(5),
pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
"""

def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
    stack = []
    j = 0
    
    for i in pushed:
        stack.append(i)
        while(len(stack)>0 and stack[-1] == popped[j]):
            stack.pop()
            j+=1
            
    return len(stack) == 0

	
def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
    i = 0
    j = 0
    
    for val in pushed:

        pushed[i] = val
        i+=1
        while(i > 0 and pushed[i - 1] == popped[j]):
            i-=1
            j+=1
            
    return i == 0
	
