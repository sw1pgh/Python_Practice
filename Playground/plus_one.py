from typing import List

class Solution:
    def plusOne(self, digits: List[int]):
        num = int("".join(map(str, digits)))
        return print([int(digit) for digit in str(num + 1)])
        
Solution().plusOne(digits = [4,3,2,1])