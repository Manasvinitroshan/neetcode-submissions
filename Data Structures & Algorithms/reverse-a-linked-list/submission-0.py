# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head # the entire linked list
        prev = None

        while curr:
            temp = curr.next #curr.next is the whole branch of the linked list past head
            curr.next = prev
            prev = curr
            curr = temp


        return prev # whole list backwards




       
        