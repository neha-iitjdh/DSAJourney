class Solution(object):
    def containsDuplicate(self, nums):
        ans = False
        nums.sort()
        for i in range(len(nums)-1):
            if(nums[i]==nums[i+1]):
                return True
        return ans

# Complexity is O(n log n) for time and O(1) for space.
# Still taking too much of execution time