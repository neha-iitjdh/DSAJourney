1class Solution:
2    def longestPalindrome(self, s: str) -> int:
3        freq = {}
4        for char in s:
5            freq[char] = freq.get(char, 0) + 1
6        length = 0
7        has_odd = False
8        
9        for count in freq.values():
10            length += (count // 2) * 2
11            if count % 2 == 1:
12                has_odd = True
13        if has_odd:
14            length += 1
15        
16        return length
17        