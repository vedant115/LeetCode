# LeetCode 104

'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 3
'''

# DFS
def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
  
# BFS
def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    
    level = 0
    q = deque([root])
    
    while q:
        for i in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level += 1
    return level
  
