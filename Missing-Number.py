class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        miss=0
        for i in range(len(nums)+1):
            if i in nums:
                pass
            else:
                return i