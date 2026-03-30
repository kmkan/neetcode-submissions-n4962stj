# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def good(node, max_val):
            if not node:
                return 0
            good_node = 1 if node.val >= max_val else 0
            if good_node:
                print(node, node.val)
            max_val = max(max_val, node.val)

            return good_node + good(node.left, max_val) + good(node.right, max_val)
        
        if not root:
            return 0
        return good(root, root.val)