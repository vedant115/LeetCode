# LeetCode 74. 

"""
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
 
Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
"""

# 1D Brute Force
def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    if target < matrix[0][0] and target > matrix[-1][-1]:
        return False
    else:
        for row in matrix:
            if target <= row[-1]:
                for i in row:
                    if i == target:
                        return True
                return False
              
# Binary Search Iterative
def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    lo, hi = 0, len(matrix) - 1
    while lo <= hi:
        midRow = (lo + hi) // 2
        row = matrix[midRow]
        if target < row[0]: hi = midRow - 1
        elif target > row[-1]: lo = midRow + 1
        else:
            l, h = 0, len(row) - 1
            while l <= h:
                mid = (l + h) // 2
                if row[mid] == target: return True
                elif target > row[mid]: l = mid + 1
                else: h = mid - 1
            return False
          
# Binary Search iterative by visualizing as a 1D array
def searchMatrix(self, matrix: List[List[int]], target: int):
    lo, hi = 0, len(matrix) * len(matrix[0]) - 1
    
    while lo <= hi:
        mid = (lo + hi) // 2
        r = mid // len(matrix[0])
        c = mid % len(matrix[0])
        if matrix[r][c] == target: return True
        if target > matrix[r][c]: lo = mid + 1
        else: hi = mid - 1
    return False
  
