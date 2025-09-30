class Solution:
    def reverse(self, x: int) -> int:
        #Approach1
        # new_num=0
        # sign = -1 if(x<0) else 1
        # x=abs(x)
        # while(x!=0):
        #     dig = x%10
        #     new_num = new_num*10 +dig
        #     x = int(x/10)
        # return sign*new_num if (-2147483648 <= sign*new_num <= 2147483647) else 0
        int_max = 2**31
        int_min = -2**31
        if x > int_max:
            return 0
        if x < int_min:
            return 0

        sign = 1
        if x < 0:
            sign = -1
        x_abs = str(abs(x))
        

        rev = x_abs[::-1]
        x_rev=  sign* int(rev)
        if x_rev > int_max:
            return 0
        if x_rev < int_min:
            return 0
        return x_rev