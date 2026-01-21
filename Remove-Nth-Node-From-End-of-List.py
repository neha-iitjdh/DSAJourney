1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
8        # Brute Force
9        # length = 0
10        # current = head
11        # while current:
12        #     length += 1
13        #     current = current.next
14        # position_from_start = length - n
15        # if position_from_start == 0:
16        #     return head.next
17        # current = head
18        # for i in range(position_from_start - 1):
19        #     current = current.next
20        # current.next = current.next.next
21        # return head
22        # Use a dummy node to handle edge cases (like removing head)
23        dummy = ListNode(0)
24        dummy.next = head
25        
26        fast = dummy
27        slow = dummy
28        for i in range(n + 1):
29            fast = fast.next
30        while fast:
31            fast = fast.next
32            slow = slow.next      
33        slow.next = slow.next.next        
34        return dummy.next
35        