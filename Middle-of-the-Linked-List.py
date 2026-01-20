1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        length = 0
9        current = head
10        while current:
11            length += 1
12            current = current.next
13        
14        middle_pos = length // 2          
15        current = head
16        for i in range(middle_pos):
17            current = current.next
18        
19        return current
20        