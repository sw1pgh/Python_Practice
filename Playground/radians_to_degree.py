import math
class Solution:
    def rad2Deg(self, rad: float) -> float:
        degree_value = rad * (180 / math.pi)
        return round(degree_value, 5)
    
print(Solution().rad2Deg(1))