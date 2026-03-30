# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur_node = head

        cur_reversed = None

        while cur_node:
            cur_reversed = ListNode(cur_node.val, cur_reversed)
            cur_node = cur_node.next
        
        return cur_reversed