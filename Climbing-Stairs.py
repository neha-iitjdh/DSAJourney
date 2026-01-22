1class Solution:
2    def climbStairs(self, n: int) -> int:
3        # if n == 1:
4        #     return 1
5        # if n == 2:
6        #     return 2        
7        # dp = [0] * (n + 1)
8        # dp[1] = 1 
9        # dp[2] = 2         
10        # for i in range(3, n + 1):
11        #     dp[i] = dp[i-1] + dp[i-2]  
12        
13        # return dp[n]
14        # space optimized
15        if n == 1:
16            return 1
17        if n == 2:
18            return 2
19        prev2 = 1  
20        prev1 = 2 
21        
22        for i in range(3, n + 1):
23            current = prev1 + prev2
24            prev2 = prev1
25            prev1 = current
26        
27        return prev1
28        