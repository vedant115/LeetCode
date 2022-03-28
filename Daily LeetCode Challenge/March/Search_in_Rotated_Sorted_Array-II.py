# LeetCode 81. 

"""
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.

Example 1:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
"""

# Linear Search
def search(self, nums: List[int], target: int) -> bool:
    for num in nums:
        if num == target:
            return True
    return False

# Binary Search
def search(self, nums: List[int], target: int) -> bool:
    """
    1 Calculate the mid index.
    2 Check if the mid element == target, return True else move to next step.
    3 Else if the mid element >= left.
          if mid element >= target and and left <= target, then shift right to mid-1 position, else shift left to mid+1 position.
    4 Else,
          If target >= mid element and target <=right, then shift left to mid+1 position, else shift right to mid-1 position. 
    5 If the element is not found return False
    """
    # If the length of the given array list is 1, then check the first element and return accordingly
    if len(nums)==1:
        if nums[0]!=target:
            return False
        else:
            return True
					
    left=0
    right=len(nums)-1
		
    # binary search 
    while(left<=right):
        # shifting to remove duplicate elements
        while left<right and nums[left] == nums[left+1]:
            left+=1
        while left<right and nums[right] == nums[right-1]:
            right-=1
						
        # step 1 calculate the mid    
        mid=(left+right)//2
				
        #step 2
        if nums[mid]==target:
            return True
					
        #step 3
        elif nums[left]<=nums[mid]:
            if nums[mid]>=target and nums[left]<=target:
                right=mid-1
            else:
                left=mid+1
								
        # step 4
        else:
            if target>=nums[mid] and target<=nums[right]:
                left=mid+1
            else:
                right=mid-1
								
    # step 5
    return False
	
