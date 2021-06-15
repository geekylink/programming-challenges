# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        sHead = ListNode()
        sNode = sHead
        
        while l1 or l2:
            if l1 and l2:
                if l1.val <= l2.val:
                    sNode.val = l1.val
                    l1 = l1.next
                else:
                    sNode.val = l2.val
                    l2 = l2.next
            elif l1:
                sNode.val = l1.val
                l1 = l1.next
            elif l2:
                sNode.val = l2.val
                l2 = l2.next
            
            if l1 or l2:
                sNode.next = ListNode()
            sNode = sNode.next
        
        return sHead
        
