class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # if(len(nums)==1):
        #     return True
        # seen=[]
        # i=0
        # while(i<len(nums)):
        #     i=i+nums[i]
        #     if i in seen:
        #         return False
        #     seen.append(i)
        #     if(i>=len(nums)-1):
        #         return True
        # return False
        maxReach = 0
        for i, step in enumerate(nums):
            if i > maxReach:
                return False
            maxReach = max(maxReach, i + step)
        return True   