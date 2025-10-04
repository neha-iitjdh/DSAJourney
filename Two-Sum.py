class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Will fail for unsorted array
        # fp=0
        # lp=len(nums)-1
        # result=[]
        # temp=nums.copy()
        # nums.sort()
        # while(fp<lp):
        #     if(nums[fp]+nums[lp]!=target):
        #         sums = nums[fp]+nums[lp]
        #         if sums>target:
        #             lp-=1
        #         else:
        #             fp+=1
        #     else:
        #         result.append(temp.index(nums[fp]))
        #         result.append(temp.index(nums[lp]))
        #         return result
        #Approach 2
        # result=[]
        # for i in range(len(nums)):
        #     comple = target-nums[i]
        #     if comple in nums[i+1:]:
        #         result.append(i)
        #         result.append(nums[i+1:].index(comple)+1+i)
        #         return result
        seen = {}
        for i, num in enumerate(nums):
            if (target - num) in seen:
                return [seen[target - num], i]
            seen[num] = i
        return None


                
        