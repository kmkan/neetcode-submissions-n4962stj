# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def search(cur, p, q):
            if p.val < cur.val and q.val < cur.val:
                return search(cur.left, p, q)
            elif p.val > cur.val and q.val > cur.val:
                return search(cur.right, p, q)
            else:
                return cur
        
        return search(root, p, q)