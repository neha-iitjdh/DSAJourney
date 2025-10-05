class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #Approach 1 (but failing for some)
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
        #Approach 2
        # maxReach = 0
        # for i, step in enumerate(nums):
        #     if i > maxReach:
        #         return False
        #     maxReach = max(maxReach, i + step)
        # return True 
        #Approach 3
        goal = len(nums)-1

        for i in range(len(nums)-1,-1,-1):
            if i +nums[i]>=goal:
                goal=i
        return True if goal==0 else False
