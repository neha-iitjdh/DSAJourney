class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #Approach1
        # n=len(nums)
        # for i in range(n):
        #     for j in range(i+1,min(i+k+1,n)):
        #         if nums[i]==nums[j]:
        #             return True
        # return False
        seen={}
        for i,num in enumerate(nums):
            if num in seen and i-seen[num]<=k:
                return True
            seen[num]=i
        return False