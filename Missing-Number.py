class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #approach 1
        # miss=0
        # for i in range(len(nums)+1):
        #     if i in nums:
        #         pass
        #     else:
        #         return i
        n = len(nums)
        return int((n*(n+1)/2)-(sum(nums)))