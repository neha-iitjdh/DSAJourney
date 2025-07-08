class Solution(object):
    def containsDuplicate(self, nums):
        temp=set(nums)
        return len(temp) !=len(nums)