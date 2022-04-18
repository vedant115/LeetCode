# LeetCode 230. 

"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        pos = 0
        ans = 0
        
        current = root
        
        while current and pos < k:
            
            if not current.left:
                pos += 1
                ans = current.val
                current = current.right
            
            else:
                pre = current.left
                while pre.right:
                    pre = pre.right
                
                pre.right = current
                left = current.left
                current.left = None
                current = left
        
        return ans
			
