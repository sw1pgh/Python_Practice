from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return print([num_map[complement], i])
            num_map[num] = i
        return []

Solution().twoSum(nums = [2,7,11,15], target = 9)            
Solution().twoSum(nums = [3,2,4], target = 6)
Solution().twoSum(nums = [3,3], target = 6)
Solution().twoSum(nums = [3,2,3], target = 6)