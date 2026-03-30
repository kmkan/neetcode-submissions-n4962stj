# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = []
        current = root

        while current or stack:
            while current:
                current.left, current.right = current.right, current.left
                ans.append(current.val)
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            current = current.right
        
        ans.reverse()
        return ans