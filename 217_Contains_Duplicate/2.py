class Solution(object):
    def containsDuplicate(self, nums):
        ans = False
        temp=set()
        for i in nums:
            if i in temp:
                return True
            else:
                temp.add(i)
        return ans

