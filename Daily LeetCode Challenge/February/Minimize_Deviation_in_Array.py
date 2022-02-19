# LeetCode 1675

'''
You are given an array nums of n positive integers.

You can perform two types of operations on any element of the array any number of times:

If the element is even, divide it by 2.
For example, if the array is [1,2,3,4], then you can do this operation on the last element, and the array will be [1,2,3,2].
If the element is odd, multiply it by 2.
For example, if the array is [1,2,3,4], then you can do this operation on the first element, and the array will be [2,2,3,4].
The deviation of the array is the maximum difference between any two elements in the array.

Return the minimum deviation the array can have after performing some number of operations.

Example 1:
Input: nums = [1,2,3,4]
Output: 1

Explanation: You can transform the array to [1,2,3,2], then to [2,2,3,2], then the deviation will be 3 - 2 = 1.
'''

def minimumDeviation(self, nums: List[int]) -> int:
	from sortedcontainers import SortedList
	
	for i in range(len(nums)):
		if nums[i]%2!=0:
			nums[i]=nums[i]*2
	
	nums = SortedList(nums)
	
	result = 100000000000
	
	while True:
		min_value = nums[0]
		max_value = nums[-1]
		if max_value % 2 == 0:
			nums.pop()
			nums.add(max_value // 2)
			max_value = nums[-1]
			min_value = nums[0]
			result = min(result , max_value - min_value)
		else:
			result = min(result , max_value - min_value)
			break
	return result
    
