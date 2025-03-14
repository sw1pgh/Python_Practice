from bisect import bisect_left
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect_left(nums, target)

# Test cases
print(Solution().searchInsert(nums=[1,3,5,6], target=0))  # Output: 0
print(Solution().searchInsert(nums=[1,3,5,6], target=2))  # Output: 1
print(Solution().searchInsert(nums=[1,3,5,6], target=7))  # Output: 4