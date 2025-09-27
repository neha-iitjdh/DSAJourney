class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        fp = 0
        lp = 1
        count = 0
        for _ in range(len(nums) - 1):
            if nums[fp] == nums[lp]:  # duplicate detected
                count = count + 1
                lp = lp + 1
            else:
                temp = nums[fp + 1]
                nums[fp + 1] = nums[lp]
                nums[lp] = temp
                lp = lp + 1
                fp = fp + 1
        return len(nums) - count
