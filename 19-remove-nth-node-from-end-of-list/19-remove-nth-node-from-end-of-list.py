# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:        
        count=0
        curr=curr2=head
        while curr is not None:
            count+=1
            curr=curr.next
        step=0
        while curr2 is not None:
            step+=1
            if count-n==0:
                return head.next
            if step==(count-n):
                curr2.next=curr2.next.next
            else:
                curr2=curr2.next            
        return head
            
        