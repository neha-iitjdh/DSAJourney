1class Solution:
2    def addStrings(self, num1: str, num2: str) -> str:
3        i = len(num1) - 1
4        j = len(num2) - 1
5        carry = 0
6        result = ""
7
8        while i >= 0 or j >= 0 or carry:
9            digit1 = int(num1[i]) if i>=0 else 0
10            digit2 = int(num2[j]) if j>=0 else 0
11            total = digit1 + digit2 + carry
12            carry = total // 10
13            digit = total % 10
14            result = result + (str(digit))
15            i -= 1
16            j -= 1
17        return result[::-1]
18        