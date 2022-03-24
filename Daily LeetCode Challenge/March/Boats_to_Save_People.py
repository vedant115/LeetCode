# LeetCode 881. 

"""
You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.

Example 1:
Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)

Example 2:
Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)
"""

def numRescueBoats(self, people: List[int], limit: int) -> int:
    boatCount = 0
    people.sort()
    
    left = 0
    right = len(people) - 1
    
    while(left <= right):
        s = people[left] + people[right]
        if(s <= limit):
            boatCount+=1
            left+=1
            right-=1
        else:
            boatCount+=1
            right-=1
        
    return boatCount
	
#-------------------------------------------------------------------------#

def numRescueBoats(self, people: List[int], limit: int) -> int:
    boatCount = 0
    people.sort()
    
    left = 0
    right = len(people) - 1
    
    while(left <= right):
        boatCount+=1
        if(people[left] + people[right] <= limit):
            left+=1
        right-=1
				
    return boatCount
	
