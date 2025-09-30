class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()        
        while n != 1 and n not in seen:
            seen.add(n)
            sumo = 0
            while n > 0:
                dig = n % 10
                n //= 10
                sumo += dig ** 2
            n = sumo        
        return n == 1
        
        

        