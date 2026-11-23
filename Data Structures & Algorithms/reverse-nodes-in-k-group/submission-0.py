class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            # 1. find the k-th node of this group
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next   # fewer than k left, done
            group_next = kth.next

            # 2. reverse the group; first node will point to group_next
            prev, curr = group_next, group_prev.next
            while curr != group_next:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            # 3. reconnect: group_prev -> new head (kth), move to new tail
            old_first = group_prev.next
            group_prev.next = kth
            group_prev = old_first