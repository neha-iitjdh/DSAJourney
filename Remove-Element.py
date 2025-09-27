class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        fp=0
        for lp in range(len(nums)):
            if(nums[lp]!=val):
                nums[fp]=nums[lp]
                fp+=1
        return fp
        