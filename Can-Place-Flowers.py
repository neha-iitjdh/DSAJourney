1class Solution:
2    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
3            count = 0
4            i = 0
5            
6            while i < len(flowerbed):
7                if flowerbed[i] == 1:
8                    i += 2  # Jump to i+2
9                else:
10                    # Current is 0, check neighbors
11                    prev_empty = (i == 0) or (flowerbed[i-1] == 0)
12                    next_empty = (i == len(flowerbed) - 1) or (flowerbed[i+1] == 0)
13                    
14                    if prev_empty and next_empty:
15                        flowerbed[i] = 1
16                        count += 1
17                        if count >= n:
18                            return True
19                        i += 2  # Jump after planting
20                    else:
21                        i += 1  # Can't plant, move one step
22            
23            return count >= n
24        