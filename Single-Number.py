class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #approach 1
        #return (2*sum(set(nums))-sum(nums))
        #approach2
        number = 0
        for num in nums:
            number = number ^ num
        return number
        