# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        ptr1 = list1
        prev = None
        while list2 != None and ptr1 != None:
            if list2.val <= ptr1.val:
                if prev:
                    prev.next = list2
                else:
                    list1 = list2
                next2 = list2.next
                prev = list2
                prev.next = ptr1
                list2 = next2
            else:
                prev = ptr1
                ptr1 = ptr1.next
        if prev:
            prev.next = ptr1 if ptr1 else list2
        return list1