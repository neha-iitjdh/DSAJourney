class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        numeric = 0
        for i in digits :
            numeric = numeric*10+i
        new_numeric = numeric+1
        return [int(i) for i in str(new_numeric)]

        