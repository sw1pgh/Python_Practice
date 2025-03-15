class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        rev = s.rstrip(" ")[::-1]  # Reverse only once using slicing (faster)
        for i in range(len(rev)):
            if rev[i] == " ":
                return i
        return len(rev)  # If no space is found, return full length
    
print(Solution().lengthOfLastWord(s="luffy is still joyboy"))