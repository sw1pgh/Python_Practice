class Solution:
    def strPal(self, input_str: str) -> bool:
        
        rev_str = input_str[::-1]
     
        li_1 = [1,4,5,8,9,111]
        
        li_2 = li_1[::-1]
        print(li_2)
        
        return print(rev_str.lower() == input_str.lower())
    
    
Solution().strPal('Dad')