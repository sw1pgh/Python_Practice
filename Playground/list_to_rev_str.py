# List to a Reversed String

from typing import List

class Rev:
    def list_2_rev_str(self, nums: List[str]) -> str:
        rev_str = list(reversed(''.join(nums)))
        print(type(str(rev_str)))
        return rev_str
    
print(Rev().list_2_rev_str(nums = ['1,2,3,4,5,6']))