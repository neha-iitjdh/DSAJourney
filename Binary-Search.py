1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3            left = 0
4            right = len(nums) - 1
5            
6            
7            while left <= right:
8                
9                mid = left + (right - left) // 2
10                
11                
12                if nums[mid] == target:
13                    return mid 
14                
15                elif nums[mid] < target:
16                   
17                    left = mid + 1  
18                
19                else:  
20                   
21                    right = mid - 1  
22            
23            
24            return -1
25                