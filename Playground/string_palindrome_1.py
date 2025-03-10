class Solution:
    def strPal(self, input_str: str) -> bool:
        
        rev_str = input_str[::-1]
        return print(rev_str.lower() == input_str.lower())

Solution().strPal('Dad')