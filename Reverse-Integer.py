class Solution:
    def reverse(self, x: int) -> int:
        new_num=0
        sign = -1 if(x<0) else 1
        x=abs(x)
        while(x!=0):
            dig = x%10
            new_num = new_num*10 +dig
            x = int(x/10)
        return sign*new_num if (-2147483648 <= sign*new_num <= 2147483647) else 0