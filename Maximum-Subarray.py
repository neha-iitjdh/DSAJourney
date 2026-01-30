1class Solution:
2    def maxSubArray(self, nums: List[int]) -> int:
3        # Brute Force Approach
4        # max_sum=float('-inf')
5
6        # for i in range(len(nums)):
7        #     for j in range(i,len(nums)):
8        #         current_sum = sum(nums[i:j+1])
9        #         max_sum = max(max_sum,current_sum)
10
11        # return max_sum
12        # Optimzed
13        # max_sum = current_sum = nums[0]
14    
15        # for i in range(1, len(nums)):
16        #     # Key decision: extend or reset?
17        #     if current_sum < 0:
18        #         current_sum = nums[i]
19        #     else:
20        #         current_sum += nums[i]
21            
22        #     max_sum = max(max_sum, current_sum)
23        
24        # return max_sum
25        # DP way
26        n = len(nums)
27    
28        # currentSum = max sum ending at current position
29        currentSum = nums[0]
30        maxSum = nums[0]
31        
32        for i in range(1, n):
33            # Either extend the previous subarray or start fresh
34            currentSum = max(currentSum + nums[i], nums[i])
35            # Update the global max
36            maxSum = max(maxSum, currentSum)
37        
38        return maxSum