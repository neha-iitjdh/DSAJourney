class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Approach1
        # numeric = 0
        # for i in digits :
        #     numeric = numeric*10+i
        # new_numeric = numeric+1
        # return [int(i) for i in str(new_numeric)]
        x=int(''.join([str(i) for i in digits]))
        y=[int(j) for j in str(x+1)]
        return y

        