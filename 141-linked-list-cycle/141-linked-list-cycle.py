# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        val=set()
        if not head:
            return False
        while head is not None:
            if head in val:
                return True
            val.add(head)
            head=head.next
        return False
        