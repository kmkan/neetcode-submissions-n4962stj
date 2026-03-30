# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        while fast and n > 0:
            fast = fast.next
            n -= 1
        
        prev = None
        while fast:
            fast = fast.next
            prev = slow
            slow = slow.next
        
        prev.next = prev.next.next
        return dummy.next