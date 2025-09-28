class Solution:
    def isPalindrome(self, s: str) -> bool:
        #APPROACH 1 but time exceeding
        # fp=0
        # lp=len(s)-1
        # while fp<=lp:
        #     if(s[fp].isalnum())==False:
        #         fp+=1
        #         continue
        #     if(s[lp].isalnum())==False:
        #         lp-=1
        #         continue
        #     if(s[fp].lower()!=s[lp].lower()):
        #         return False
        #     fp+=1
        #     lp-=1
        # return True
        ss = s.strip().lower()
        l = []
        for i in ss:
            if i.isalnum():
                l.append(i)
        return l == l[::-1]