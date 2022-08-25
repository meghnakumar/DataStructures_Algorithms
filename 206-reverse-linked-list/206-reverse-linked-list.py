# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.rev(head)
    
    def rev(self,head, prev=None):
        if not head:
            return prev
        curr=head.next
        head.next=prev
        return self.rev(curr,head)
        
        