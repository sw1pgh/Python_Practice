from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range (len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
                
        return print(nums, ' ', k)
    
Solution().removeElement(nums = [3,2,2,3], val = 3)
Solution().removeElement(nums = [0,1,2,2,3,0,4,2], val = 2)

'''
Can be done with remove() too

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while (i < len(nums)):
            if (nums[i] == val):
                nums.remove(nums[i])
            else:
                i += 1
        return len(nums)
'''