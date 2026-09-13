# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        #find the middle of the linked list

        fast = head
        slow = head
        first = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #reverse second part of the list
        second = slow.next
        slow.next = prev = None
        curr = second

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        #merge alternatively

        l1 = first
        l2 = prev

        while prev:
            tmp1 = first.next
            tmp2 = prev.next

            first.next = prev
            prev.next = tmp1

            first = tmp1
            prev = tmp2


        
        



        