1class Solution:
2    def lemonadeChange(self, bills: List[int]) -> bool:
3        five_count = 0
4        ten_count = 0
5            
6        for bill in bills:
7            if bill == 5:
8                
9                five_count += 1
10                
11            elif bill == 10:
12                
13                if five_count >= 1:
14                    five_count -= 1 
15                    ten_count += 1 
16                else:
17                    return False  
18                    
19            else:  
20               
21                if ten_count >= 1 and five_count >= 1:
22                    ten_count -= 1
23                    five_count -= 1
24                
25                elif five_count >= 3:
26                    five_count -= 3
27                else:
28                    return False 
29        return True 
30        