1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        dummy = ListNode(0)
9        dummy.next = head        
10        prev = dummy  
11        current = head        
12        while current:
13            is_duplicate = False            
14            while current.next and current.val == current.next.val:
15                is_duplicate = True
16                current = current.next            
17            if is_duplicate:
18                current = current.next
19                prev.next = current
20            else:
21                prev = current
22                current = current.next        
23        return dummy.next
24        