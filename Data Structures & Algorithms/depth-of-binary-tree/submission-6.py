# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = []
        max_depth = 0
        cur_depth = 0
        current = root

        while current or stack:
            while current:
                cur_depth += 1
                stack.append((current, cur_depth))
                current = current.left
            
            current, cur_depth = stack.pop()
            max_depth = max(max_depth, cur_depth)
            current = current.right
        
        return max_depth