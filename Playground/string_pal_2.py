class Solution:
    def strPAL(self, input_string) -> bool:
        
        rev_str = ''.join(reversed(input_string))
        return print(rev_str.lower() == input_string.lower())
    
Solution().strPAL('Swapnaneel Ghosh')