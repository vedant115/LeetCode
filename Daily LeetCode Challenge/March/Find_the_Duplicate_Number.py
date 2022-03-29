# LeetCode 287. 

"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
"""

def findDuplicate(self, nums: List[int]) -> int:
    s = set()
    for i in nums:
        if i in s:
            return i
        else:
            s.add(i)
						
#-------------------------------------------------------------#

def findDuplicate(self, nums: List[int]) -> int:
    # Floyd Algorithm
    # step1: turtle moves one step, hare moves two steps
    # step2: turtle meet hare, reset turtle and slow down hare
    # step3: turtle meet hare, 
    # time complexity(n)
    # space complexity(1)
    
    turtle = 0
    hare = 0
    step1 = 1
    step2 = 2
    while True:
        turtle = nums[turtle]
        for i in range(step2):
            hare = nums[hare]
        if turtle==hare:
            if step2==2:
                turtle = 0
                step2 = 1
            else:
                return turtle
	
