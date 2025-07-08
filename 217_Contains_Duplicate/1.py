class Solution(object):
    def containsDuplicate(self, nums):
        ans = False
        temp=[]
        for i in nums:
            if i in temp:
                return True
            else:
                temp.append(i)
        return ans

# Working for basic test cases but TLE for large inputs.
# Complexity is O(n) for time and O(n) for space.