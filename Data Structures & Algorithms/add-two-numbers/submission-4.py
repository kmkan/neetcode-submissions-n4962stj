# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev_l1 = None
        cur_l1 = l1
        cur_l2 = l2
        carry = 0
        while cur_l1 and cur_l2:
            prev_l1 = cur_l1
            total = cur_l1.val + cur_l2.val + carry
            cur_val = total % 10
            carry = total // 10
            cur_l1.val = cur_val
            cur_l1 = cur_l1.next
            cur_l2 = cur_l2.next
        
        if cur_l1:
            while cur_l1:
                prev_l1 = prev_l1.next
                total = cur_l1.val + carry
                cur_val = total % 10
                carry = total // 10
                cur_l1.val = cur_val
                cur_l1 = cur_l1.next
        elif cur_l2:
            prev_l1.next = cur_l2
            while cur_l2:
                prev_l1 = prev_l1.next
                total = cur_l2.val + carry
                cur_val = total % 10
                carry = total // 10
                cur_l2.val = cur_val
                cur_l2 = cur_l2.next
        if carry:
            prev_l1.next = ListNode(carry, None)
        return l1
        
