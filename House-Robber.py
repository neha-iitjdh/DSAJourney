1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        n = len(nums)
4    
5        # Edge cases
6        if n == 0:
7            return 0
8        if n == 1:
9            return nums[0]
10        
11        # Create DP array
12        maxMoney = [0] * n
13        maxMoney[0] = nums[0]
14        maxMoney[1] = max(nums[0], nums[1])
15        
16        # Fill the array
17        for i in range(2, n):
18            maxMoney[i] = max(maxMoney[i-1], nums[i] + maxMoney[i-2])
19        
20        return maxMoney[n-1]
21        