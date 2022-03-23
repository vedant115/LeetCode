# LeetCode 991. 

"""
There is a broken calculator that has the integer startValue on its display initially. In one operation, you can:

multiply the number on display by 2, or
subtract 1 from the number on display.
Given two integers startValue and target, return the minimum number of operations needed to display target on the calculator.

Example 1:
Input: startValue = 2, target = 3
Output: 2

Explanation: Use double operation and then decrement operation {2 -> 4 -> 3}.
"""

def brokenCalc(self, startValue: int, target: int) -> int:
     result = 0
     while(target > startValue):
         if(target % 2 == 0):
             target /= 2
         else:
             target += 1 
         
         result+=1
     
     return int(result + (startValue - target))
		
		
def brokenCalc(self, startValue: int, target: int) -> int:
        
     if(startValue >= target):
         return int(startValue - target)
    
     if(target % 2 == 0):
         return 1 + self.brokenCalc(startValue, target / 2)
     
     return int(1 + self.brokenCalc(startValue, target + 1))
		
