1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        # n = len(prices)
4        # maxProfit = 0
5        
6        # # Try every buy day
7        # for i in range(n):
8        #     buyPrice = prices[i]
9            
10        #     # Try every sell day after buy day
11        #     for j in range(i + 1, n):
12        #         sellPrice = prices[j]
13        #         profit = sellPrice - buyPrice
14        #         maxProfit = max(maxProfit, profit)
15        
16        # return maxProfit
17        # -------------------------------
18        # minPrice = prices[0]  # Or use float('inf')
19        # maxProfit = 0
20        
21        # for price in prices:
22        #     # Update minimum price if we found a cheaper buy opportunity
23        #     if price < minPrice:
24        #         minPrice = price
25            
26        #     # Calculate profit if we sell today
27        #     profit = price - minPrice
28            
29        #     # Update maximum profit
30        #     if profit > maxProfit:
31        #         maxProfit = profit
32        
33        # return maxProfit
34        minPrice = float('inf')
35        maxProfit = 0
36        
37        for price in prices:
38            minPrice = min(minPrice, price)
39            maxProfit = max(maxProfit, price - minPrice)
40        
41        return maxProfit
42
43        