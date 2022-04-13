# LeetCode 59. 

"""
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

Example 1:
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:
Input: n = 1
Output: [[1]]
"""

def generateMatrix(self, n: int) -> List[List[int]]:
    left, right, top, bottom = 0, n, 0, n
    num = 1
    matrix = [[0]*n for _ in range(n)]
    while left < right and top < bottom:
        
        # left --> right
        for i in range(left, right):
            matrix[top][i] = num
            num+=1
        
        top+=1
        
        # top --> bottom
        for i in range(top, bottom):
            matrix[i][right-1] = num
            num+=1
            
        right-=1
        
        if not (left < right and top < bottom): 
            break  
        
        # right --> left
        for i in range(right-1, left-1, -1):
            matrix[bottom-1][i] = num
            num+=1
        
        bottom-=1
        
        # bottom --> top
        for i in range(bottom-1, top-1, -1):
            matrix[i][left] = num
            num+=1
            
        left+=1
        
        
    return matrix
	
