1class Solution:
2    def longestPalindrome(self, s: str) -> int:
3        # Step 1: Count character frequencies
4        freq = {}
5        for char in s:
6            freq[char] = freq.get(char, 0) + 1
7        
8        # Step 2: Calculate palindrome length
9        length = 0
10        has_odd = False
11        
12        for count in freq.values():
13            # Add the largest even number ≤ count
14            length += (count // 2) * 2
15            
16            # Track if we have any odd counts
17            if count % 2 == 1:
18                has_odd = True
19        
20        # Step 3: Add 1 for center if we have any odd count
21        if has_odd:
22            length += 1
23        
24        return length
25        