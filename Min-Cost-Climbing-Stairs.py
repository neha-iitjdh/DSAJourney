1class Solution:
2    def minCostClimbingStairs(self, cost: List[int]) -> int:
3        # n = len(cost)
4        # minCost = [0] * n
5        # minCost[0] = cost[0]
6        # minCost[1] = cost[1]
7        # for i in range(2, n):
8        #     minCost[i] = cost[i] + min(minCost[i-1], minCost[i-2])
9        # return min(minCost[n-1], minCost[n-2])
10        n = len(cost)
11        prev2 = cost[0]  
12        prev1 = cost[1]  
13        
14        for i in range(2, n):
15            current = cost[i] + min(prev1, prev2)
16            prev2 = prev1
17            prev1 = current
18        return min(prev1, prev2)
19            