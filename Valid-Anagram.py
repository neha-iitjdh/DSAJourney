1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        if len(s) != len(t):
4            return False
5        freq = {}
6        for char in s:
7            freq[char] = freq.get(char, 0) + 1
8        for char in t:
9            if char not in freq:
10                return False
11            freq[char] -= 1
12            if freq[char] < 0:
13                return False
14        for count in freq.values():
15            if count != 0:
16                return False
17        
18        return True
19            