# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        i = 0
        cur_l1 = l1
        cur_l2 = l2
        total = 0

        while cur_l1 and cur_l2:
            total = total + cur_l1.val * 10 ** i + cur_l2.val * 10 ** i
            cur_l1 = cur_l1.next
            cur_l2 = cur_l2.next
            i += 1
        
        while cur_l1:
            total = total + cur_l1.val * 10 ** i
            i += 1
            cur_l1 = cur_l1.next
        
        while cur_l2:
            total = total + cur_l2.val * 10 ** i
            i += 1
            cur_l2 = cur_l2.next
        
        dummy = ListNode(0, None)
        new_node = dummy

        while total > 0:
            new_node.next = ListNode(total % 10, None)
            new_node = new_node.next
            total //= 10
        
        if not dummy.next:
            return dummy
        return dummy.next
