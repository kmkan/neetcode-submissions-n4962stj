# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur_list1 = list1
        cur_list2 = list2

        dummy = ListNode(0, None)
        new_list = dummy
        while cur_list1 and cur_list2:
            if cur_list1.val <= cur_list2.val:
                new_list.next = ListNode(cur_list1.val, None)
                cur_list1 = cur_list1.next
            else:
                new_list.next = ListNode(cur_list2.val, None)
                cur_list2 = cur_list2.next
            new_list = new_list.next
        
        if cur_list1:
            new_list.next = ListNode(cur_list1.val, cur_list1.next)
        elif cur_list2:
            new_list.next = ListNode(cur_list2.val, cur_list2.next)
        
        return dummy.next
