class Solution:
    def isHappy(self, n: int) -> bool:
        #Approach1
        # seen = set()        
        # while n != 1 and n not in seen:
        #     seen.add(n)
        #     sumo = 0
        #     while n > 0:
        #         dig = n % 10
        #         n //= 10
        #         sumo += dig ** 2
        #     n = sumo        
        # return n == 1
        seen = set()
        while True:
            if n in seen:
                return False
            seen.add(n)
            if n == 1:
                return True
            n = sum([int(x)**2 for x in list(str(n))])
        
        

        