class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp = x
        reverse=0
        while (temp>0):
            dig = temp%10
            reverse = reverse*10 + dig
            temp = temp/10
        if (x==reverse):
            return True
        else:
            return False
        
        

