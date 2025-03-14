from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i = 1
        while (i < len(nums)):
            if nums[i - 1] == nums[i]:
                nums.pop(i)
            else:
                i += 1
                
        k = len(nums)
        
        return k
    
print(Solution().removeDuplicates(nums = [1,1,2]))
print(Solution().removeDuplicates(nums = [0,0,1,1,1,2,2,3,3,4]))