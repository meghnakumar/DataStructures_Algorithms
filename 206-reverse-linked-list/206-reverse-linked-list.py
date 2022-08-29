# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.rev(head)
    
    def rev(self,head, prev=None):
        if not head:
            return prev
        curr=head.next
        head.next=prev
        return self.rev(curr,head)
        