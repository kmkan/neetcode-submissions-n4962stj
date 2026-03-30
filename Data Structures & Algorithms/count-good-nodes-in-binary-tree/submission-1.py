# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def findNodes(node, max_val):
            if not node:
                return 0
            
            max_val = max(max_val, node.val)
            is_good = 1 if max_val <= node.val else 0

            return is_good + findNodes(node.left, max_val) + findNodes(node.right, max_val)
            
        return findNodes(root, root.val)