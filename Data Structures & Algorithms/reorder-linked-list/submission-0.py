# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        cur = slow.next
        slow.next = None

        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        
        begin = head
        dummy = ListNode(0, None)
        cur = dummy
        while prev and begin:
            cur.next = begin
            begin = begin.next
            cur = cur.next
            cur.next = prev
            prev = prev.next
            cur = cur.next
        
        if prev:
            cur.next = prev
        elif begin:
            cur.next = begin
        head = dummy.next
        
        

        
