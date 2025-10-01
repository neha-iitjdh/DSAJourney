class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if (n<=0):
            return False
        return not(math.log2(n)%1)
        