# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: ListNode | None, list2: ListNode | None
    ) -> ListNode | None:
        dummy = ret_head = ListNode()

        while list1 and list2:
            if list1.val > list2.val:
                ret_head.next = list1
                list1 = list1.next
            else:
                ret_head.next = list2
                list2.next = list2

            ret_head = ret_head.next

        if list1:
            ret_head.next = list1

        else:
            ret_head.next = list2

        return dummy.next
