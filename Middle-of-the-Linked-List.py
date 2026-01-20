1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        #brute force  approach
9        # length = 0
10        # current = head
11        # while current:
12        #     length += 1
13        #     current = current.next
14        
15        # middle_pos = length // 2          
16        # current = head
17        # for i in range(middle_pos):
18        #     current = current.next
19        
20        # return current
21        # optimized
22        slow = fast = head
23        
24        while fast and fast.next:
25            slow = slow.next      
26            fast = fast.next.next 
27        return slow
28        