class Solution:
    def isValid(self, s: str) -> bool:
        depo = []
        para_map = {')':'(',']':'[','}':'{'}
        for i in s:
            if i in para_map.values():
                depo.append(i)
            elif (i in para_map.keys() and depo[-1]==para_map[i]):
                depo.pop()
            else:
                return False
        return(len(depo)==0)
        