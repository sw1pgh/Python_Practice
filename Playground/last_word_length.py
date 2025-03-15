class Solution:
    def lastWordLength(self, s: str) -> int:
        rev = s.rstrip(' ')[::-1]
        k = 0
        for i in rev:
            if i != ' ':
                k += 1
            else:
                return k
        return len(rev)

Solution().lastWordLength(s = 'l')

# 2nd solution:
'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        rev = s.rstrip(" ")[::-1]  # Reverse only once using slicing (faster)
        for i in range(len(rev)):
            if rev[i] == " ":
                return i
        return len(rev)  # If no space is found, return full length
    
print(Solution().lengthOfLastWord(s="luffy is still joyboy"))
'''