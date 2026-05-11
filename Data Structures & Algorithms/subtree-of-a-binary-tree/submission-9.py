# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(x, y):
            if not x and not y:
                return True
            elif not x or not y or x.val != y.val:
                return False
            else:
                return same(x.left, y.left) and same(x.right, y.right)

        def check(node, subRoot):
            if not subRoot:
                return True
            elif not node and subRoot:
                return False
            else:
                return same(node, subRoot) or check(node.left, subRoot) or check(node.right, subRoot)
        
        return check(root, subRoot)
            