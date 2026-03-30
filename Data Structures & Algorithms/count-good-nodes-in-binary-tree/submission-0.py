# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        max_val = -101
        def findNodes(node, max_val):
            if not node:
                return 0
            
            if max_val <= node.val:
                max_val = max(max_val, node.val)
                return 1 + findNodes(node.left, max_val) + findNodes(node.right, max_val)
            else:
                return findNodes(node.left, max_val) + findNodes(node.right, max_val)
            
        return findNodes(root, max_val)