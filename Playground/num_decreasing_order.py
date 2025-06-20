'''
Congratulations! You are one more step close to Python Programming World. You are now familiar with if-elif-else in Python, and for loop in Python.

While loop in Python is same as like in CPP and Java, but, here you have to use ':' 
to end while statement (used to end any statement). While loop is used to iterate same as for loop, 
except that in while loop you can customize jump of steps in coupling with variable used to loop, 
after every iteration, unlike in for loop (you cannot customize jump according to the variable you are using to loop through).

Let's get it more clearly through this question. Given a number x, 
the task is to print the numbers from x to 0 in decreasing order in a single line.

Example:

Input:
x = 3

Output:
3 2 1 0

Explanation:
Numbers in decreasing order from 3
are 3, 2, 1, 0.

Your Task:
This is a function problem. You need to complete the printInDecreasing() function and print the x from x to 0 in a single line.
'''

from typing import List

class Solution:
    def printInDecreasing(self, num: int) -> List:
        while num >= 0:
            print(num, end=' ')
            num -= 1
    
Solution().printInDecreasing(num = 10)