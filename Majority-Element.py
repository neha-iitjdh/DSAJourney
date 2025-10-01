class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Approach1
        # count_list=Counter(nums)
        # max_count=max(count_list.values())
        # for i in count_list.keys():
        #     if count_list[i]==max_count:
        #         return i
        nums_dict =Counter(nums)
        return max(nums_dict , key = nums_dict.get)
        