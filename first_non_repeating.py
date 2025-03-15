class Solution:
    def firstUniqChar(self, s: str) -> int:
        i = 0
        while i < len(s) < 10^5:
            if s.count(s[i]) <= 1:
                return i
            else:
                i += 1
        return -1
        
print(Solution().firstUniqChar(s = "aabb"))

# This solution does not work for a very large string set for example n number of aaaaa....
# So alternative solution is:

'''
from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Step 1: Count occurrences of each character
        char_count = Counter(s)
        
        # Step 2: Find the first unique character
        for i, ch in enumerate(s):
            if char_count[ch] == 1:
                return i
        
        return -1  # No unique character found
'''