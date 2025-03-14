from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        for i in range (len(nums)-1,0, -1):
            if nums[i] == nums[i - 1]:
                nums.pop(i)
                
        k = len(nums)
        
        return k
    
print(Solution().removeDuplicates(nums = [1,1,2]))
print(Solution().removeDuplicates(nums = [0,0,1,1,1,2,2,3,3,4]))