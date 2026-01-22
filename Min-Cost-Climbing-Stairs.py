1class Solution:
2    def minCostClimbingStairs(self, cost: List[int]) -> int:
3        n = len(cost)
4        minCost = [0] * n
5        minCost[0] = cost[0]
6        minCost[1] = cost[1]
7        for i in range(2, n):
8            minCost[i] = cost[i] + min(minCost[i-1], minCost[i-2])
9        return min(minCost[n-1], minCost[n-2])
10            