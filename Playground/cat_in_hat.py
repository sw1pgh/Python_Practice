'''
You are given a string str, you need to return True if  the words "cat" and "hat" appear same number of times in str, otherwise return False.
Note: str contains only lowercase English alphabets.

Example 1:

Input:
str = catinahat
Output:
True
Explanation:
cat and hat both are present
1 number of times.
Example 2:

Input:
str = bazingaa
Output:
True
Explanation:
cat and hat both are present
0 number of times.
Constraints:
1 <= str.size() <= 105

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Your Task:
This is a function problem. You don't need to take any input. Just complete the function cat_hat() that takes a string str as input.
'''

class Solution:
    def cat_hat(self, str: str) -> bool:
        cat_counter = 0
        hat_counter = 0
        n = len(str)
        
        for i in range(n - 2):  # Only go up to len(str) - 3 to check 3-letter substrings
            if str[i:i+3] == 'cat':
                cat_counter += 1
            elif str[i:i+3] == 'hat':
                hat_counter += 1
                
        return cat_counter == hat_counter

# Test cases
print(Solution().cat_hat('catinahat'))   # True
print(Solution().cat_hat('bazingaa'))    # True
print(Solution().cat_hat('cathatcat'))   # False