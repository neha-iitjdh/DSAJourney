1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        if not head:
9            return head
10        
11        current = head
12        
13        while current and current.next:
14            if current.val == current.next.val:
15                # Skip the duplicate
16                current.next = current.next.next
17            else:
18                # Move to next unique value
19                current = current.next
20        
21        return head
22            