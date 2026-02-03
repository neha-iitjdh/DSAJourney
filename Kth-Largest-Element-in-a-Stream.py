1class KthLargest:
2    def __init__(self, k: int, nums: List[int]):
3        self.k = k
4        self.min_heap = []
5                
6        for num in nums:
7            self.add(num)        
8
9    def add(self, val: int) -> int:  
10        if len(self.min_heap) < self.k:
11            heapq.heappush(self.min_heap, val)        
12        
13        elif val > self.min_heap[0]:
14            heapq.heappop(self.min_heap) 
15            heapq.heappush(self.min_heap, val)            
16           
17        return self.min_heap[0]