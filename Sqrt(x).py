1class Solution:
2    def mySqrt(self, x: int) -> int:
3        # Brute Force O(root(n)) ; O(1) space
4        # if  x==0 or x==1:
5        #     return x
6        # i=1
7        # while(i*i<=x):
8        #     i+=1
9        # return (i-1)
10
11        # Binary Search Approach O(log(n))
12        if x==0 or x==1:
13            return x
14        left,right = 1,x
15        result = 0
16
17        while left <= right:
18            mid = left + (right-left) // 2
19
20            if mid * mid == x:
21                return mid
22            
23            elif mid*mid < x:
24                result = mid
25                left = mid + 1
26            
27            else:
28                right = mid-1
29
30        return  result
31