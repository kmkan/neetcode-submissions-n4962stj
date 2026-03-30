# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traversal(self, node: Optional[TreeNode], ans: List[TreeNode]) -> List[int]:
        if not node:
            return ans
        ans = self.traversal(node.left, ans)
        ans.append(node.val)
        ans = self.traversal(node.right, ans)
        return ans
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.traversal(root, [])