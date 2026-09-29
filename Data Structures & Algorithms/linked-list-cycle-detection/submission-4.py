# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        if not head:
            return False

        while slow is not None:
            if slow.next is None or fast.next is None or fast.next.next is None:
                return False

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        else:
            return False
        