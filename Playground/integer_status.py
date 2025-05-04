'''
Check the status - Python

Given two integer variables a and b, and a boolean variable flag. The task is to check the status and return accordingly.

Return True for the following cases:

Either a or b (not both) is non-negative and the flag is false.
Both a and b are negative and the flag is true.
Otherwise, return False.

Examples: 

Input: a = 1, b = -1, flag = False
Output: True
Explanation: Since a is positive, b is negative, and flag is False, condition 1 holds true, so the function returns True.
Input: a = -182, b = -9121, flag = True
Output: True
Explanation: Since both a and b are negative and flag is True, condition 2 holds true, so the function returns True.
Input: a = 5, b = 3, flag = True
Output: False
Explanation: Neither condition 1 nor condition 2 holds, so the function returns False.
Constraints:
-10 <= a, b <= 10
flag ∈ {True, False} 
'''

class Solution:
    def integer_status_checker(self, a: int, b: int, flag: bool) -> bool:
        if ((a >= 0 or b >= 0) and flag == False):
            return True
        elif((a < 0 and b < 0) and flag == True):
            return True
        else:
            return False
            
print(Solution().integer_status_checker(a = 1, b = -1, flag = False))
print(Solution().integer_status_checker(a = -182, b = -9121, flag = True))
print(Solution().integer_status_checker(a = 5, b = 3, flag = True))