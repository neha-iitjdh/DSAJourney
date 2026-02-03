1class Solution:
2    def lastStoneWeight(self, stones: List[int]) -> int:
3        max_heap = [-stone for stone in stones]
4        heapq.heapify(max_heap) 
5        
6        while len(max_heap) > 1:
7            
8            first = -heapq.heappop(max_heap)   
9            second = -heapq.heappop(max_heap)  
10            
11            
12            if first != second:
13                heapq.heappush(max_heap, -(first - second))  
14        
15        
16        return -max_heap[0] if max_heap else 0
17            