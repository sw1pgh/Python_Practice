'''Two Sums [Leet Code Problem. Must Learn.]'''

from typing import List

class Solution:
    def twoSums(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, num in enumerate(nums):
            desired_value = target - num
            if desired_value in hash_map:
                return [hash_map[desired_value], i]
            hash_map[num] = i

print(Solution().twoSums(nums = [10,10,10], target = 20))