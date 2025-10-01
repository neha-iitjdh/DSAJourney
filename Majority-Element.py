class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_list=Counter(nums)
        max_count=max(count_list.values())
        for i in count_list.keys():
            if count_list[i]==max_count:
                return i
        