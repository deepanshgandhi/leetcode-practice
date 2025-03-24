# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev = None
        curr, n = head,head.next
        while curr:
            n = curr.next
            if n and curr.val == n.val:
                while n and curr.val == n.val:
                    n = n.next
                if prev:
                    prev.next = n
                else:
                    head = n
                curr = n
            else:
                prev = curr
                curr = curr.next
        return head