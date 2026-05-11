# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0
            
            left = height(node.left)
            right = height(node.right)

            if left == -1 or right == -1:
                return -1
            
            left += 1
            right += 1

            if abs(left - right) > 1:
                return -1
            
            return max(left, right)

        
        val = height(root)
        print(val)
        if val == -1:
            return False
        return True