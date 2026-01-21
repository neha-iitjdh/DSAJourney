1class Solution:
2    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
3        note_freq = {}
4        for char in ransomNote:
5            note_freq[char] = note_freq.get(char, 0) + 1
6        
7        mag_freq = {}
8        for char in magazine:
9            mag_freq[char] = mag_freq.get(char, 0) + 1
10        
11        # Check if every character in note has enough in magazine
12        for char, count in note_freq.items():
13            if mag_freq.get(char, 0) < count:
14                return False
15        
16        return True
17        