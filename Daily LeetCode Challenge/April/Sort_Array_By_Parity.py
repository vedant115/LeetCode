# LeetCode 905. 

"""
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

 

Example 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
"""

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
		#Initially the pivot is at the end
        pivot = len(nums)-1
        
		#we start from the 0th index
        i = 0
		
		#As long as we are to the left of the pivot we only need all even numbers
        while i <= pivot:
            
			#If we find a number that is not even then...
            if nums[i]%2 != 0:
				# We swap it out with the pivot element and then decrease the pivot index as now we have only odd numbers to the right of the pivot
                nums[i], nums[pivot] = nums[pivot], nums[i]
                pivot-=1
            else:
			#but if the element was even then we just move forward
                i+=1
        
        return nums
