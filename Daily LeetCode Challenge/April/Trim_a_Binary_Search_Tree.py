# LeetCode 669. 

"""
Given the root of a binary search tree and the lowest and highest boundaries as low and high, trim the tree so that all its elements lies in [low, high]. 
Trimming the tree should not change the relative structure of the elements that will remain in the tree (i.e., any node's descendant should remain a descendant). 
It can be proven that there is a unique answer.

Return the root of the trimmed binary search tree. Note that the root may change depending on the given bounds.

Example 1:
Input: root = [1,0,2], low = 1, high = 2
Output: [1,null,2]

Example 2:
Input: root = [3,0,4,null,2,null,null,1], low = 1, high = 3
Output: [3,2,null,1]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
         def prune(node):
            # if node is null, nothing to prune, return Null
            if not node:
                return None

            # If the current node's val is higher than high, then this node and (obviously) the right subtree
            # can be omitted (as everything in the right subtree will definitely be higher than high), 
            # so only prune the left subtree and return it
            if node.val > high:
                return prune(node.left)

            # If the current node's value is less than low, then omit this node and its left subtree
            # prune the right subtree alone and return it
            if node.val < low:
                return prune(node.right)


            # if the current node's val lies in [low, high], then we may have to keep some of the left subtre,
            # some of the right subtree, and this node. 
            # so attach the pruned left subtree and the pruned right subtree and return this node
            node.left = prune(node.left)
            node.right = prune(node.right)

            return node

         return prune(root)
			
