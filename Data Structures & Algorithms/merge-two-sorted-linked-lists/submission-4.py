# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        cur_node = dummy
        cur1 = list1
        cur2 = list2

        while cur1 and cur2:
            if cur1.val <= cur2.val:
                cur_node.next = cur1
                cur1 = cur1.next
            else:
                cur_node.next = cur2
                cur2 = cur2.next
            cur_node = cur_node.next
        
        if cur1:
            cur_node.next = cur1
        else:
            cur_node.next = cur2
        
        return dummy.next


