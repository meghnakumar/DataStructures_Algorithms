# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res=ListNode(0)
        tail=res
              
        while True:
            if list1 is None:
                tail.next= list2
                break
            if list2 is None:
                tail.next= list1
                break
            if list1.val<=list2.val:
                tail.next=list1
                list1=list1.next
            else:
                tail.next=list2
                list2=list2.next
            tail=tail.next
            
        # while list1 and list2 is not None:
            
            
#         while list1 and list2 is not None:
            
#             if list1.val<list2.val:
#                 res=
#                 list1=list1.next
#             else:
#                 res=list2
#             while list2 is not None:
#                 if list1.val<list2.val:
#                     res=list1
#                 else:
#                     res=list2
#                 list2=list2.next
#             list1=list1.next
        
        return res.next
        