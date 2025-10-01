class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Approach1
        # count_list=Counter(nums)
        # max_count=max(count_list.values())
        # for i in count_list.keys():
        #     if count_list[i]==max_count:
        #         return i
        #Approach2
        # nums_dict =Counter(nums)
        # return max(nums_dict , key = nums_dict.get)
        #Approach3
        # element=nums[0]
        # c=1
        # n=len(nums)
        # for i in range(1,n):
        #     if nums[i]==element:
        #         c+=1
        #     else:
        #         c-=1
        #         if c==0:
        #             element=nums[i]
        #             c=1
        # return element
        #Approach 4
        # nums.sort()
        # n = len(nums)
        # return nums[n//2]
        #Approach5
        return max(set(nums), key=nums.count)
        