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
13        max_sum = current_sum = nums[0]
14    
15        for i in range(1, len(nums)):
16            # Key decision: extend or reset?
17            if current_sum < 0:
18                current_sum = nums[i]  # Reset (start fresh)
19            else:
20                current_sum += nums[i]  # Extend (keep building)
21            
22            max_sum = max(max_sum, current_sum)
23        
24        return max_sum