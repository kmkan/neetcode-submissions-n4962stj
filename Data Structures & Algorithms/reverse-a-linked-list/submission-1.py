# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reverse_node = None
        cur_node = head

        while cur_node:
            reverse_node = ListNode(cur_node.val, reverse_node)
            cur_node = cur_node.next
        
        return reverse_node