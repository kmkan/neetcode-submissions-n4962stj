# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        cur_second_half = slow.next
        prev_second_half = None
        slow.next = None

        while cur_second_half:
            next_second_half = cur_second_half.next
            cur_second_half.next = prev_second_half
            prev_second_half = cur_second_half
            cur_second_half = next_second_half
        
        cur_first_half = head
        cur = dummy

        while prev_second_half:
            cur.next = cur_first_half
            cur_first_half = cur_first_half.next
            cur = cur.next
            cur.next = prev_second_half
            prev_second_half = prev_second_half.next
            cur = cur.next
        
        if cur_first_half:
            cur.next = cur_first_half
        
        head = dummy.next





        
