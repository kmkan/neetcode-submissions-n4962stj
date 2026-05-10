# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, None)

        cur = dummy
        list1_node = list1
        list2_node = list2
        while list1_node and list2_node:
            if list1_node.val <= list2_node.val:
                cur.next = list1_node
                list1_node = list1_node.next
            else:
                cur.next = list2_node
                list2_node = list2_node.next
            cur = cur.next
    
        if list1_node:
            cur.next = list1_node
        if list2_node:
            cur.next = list2_node
        
        return dummy.next