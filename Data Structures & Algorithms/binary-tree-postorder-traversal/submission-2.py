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

        while stack or current:
            while current:
                ans.append(current.val)
                stack.append(current)
                current = current.right
            
            current = stack.pop()
            current = current.left
        
        ans.reverse()
        return ans