class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #Approach1
        #return int((3*sum(set(nums))-sum(nums))/2)
        #Approach2
        counts = Counter(nums)
        once = [item for item, count in counts.items() if count == 1]
        return once[0]