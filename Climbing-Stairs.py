1class Solution:
2    def climbStairs(self, n: int) -> int:
3        if n == 1:
4            return 1
5        if n == 2:
6            return 2        
7        dp = [0] * (n + 1)
8        dp[1] = 1 
9        dp[2] = 2         
10        for i in range(3, n + 1):
11            dp[i] = dp[i-1] + dp[i-2]  
12        
13        return dp[n]
14        