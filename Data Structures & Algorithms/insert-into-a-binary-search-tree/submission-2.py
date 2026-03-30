# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            root = TreeNode(val)
            return root
        def insert(root):
            if not root.left and val < root.val:
                root.left = TreeNode(val)
                return
            elif not root.right and val > root.val:
                root.right = TreeNode(val)
                return
            elif val < root.val:
                return insert(root.left)
            else:
                return insert(root.right)
        
        insert(root)
        return root
    