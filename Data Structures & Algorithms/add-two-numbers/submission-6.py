# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur_l1, cur_l2 = l1, l2
        prev = None
        carry = 0
        while cur_l1 and cur_l2:
            prev = cur_l1
            total = cur_l1.val + cur_l2.val + carry
            cur_val = total % 10
            carry = total // 10
            cur_l1.val = cur_val
            cur_l1 = cur_l1.next
            cur_l2 = cur_l2.next
        
        if cur_l2:
            prev.next = cur_l2
            cur_l1 = cur_l2

        while cur_l1:
            prev = cur_l1
            total = cur_l1.val + carry
            cur_val = total % 10
            carry = total // 10
            cur_l1.val = cur_val
            cur_l1 = cur_l1.next
        
        if carry:
            prev.next = ListNode(carry, None)
        return l1
        
