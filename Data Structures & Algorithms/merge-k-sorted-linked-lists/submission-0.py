# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        res = ListNode()

        while(len(lists) > 1):
            merged_list = []

            for r in range(0,len(lists),2):
                list1 = lists[r]
                list2 = lists[r+1] if r+1 < len(lists) else None
                merge = self.mergeLists(list1, list2)
                merged_list.append(merge)
            lists = merged_list
        return lists[0]

            
    
    def mergeLists(self, list1, list2) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return dummy.next

                
        