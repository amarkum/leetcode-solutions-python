"""
https://leetcode.com/problems/sqrtx/

Given a non-negative integer x, compute and return the square root of x.
Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

Example 1:

Input: x = 4
Output: 2
"""

class SquareRootX:
    def mySqrt(self, x: int) -> int:
        y = 0
        while y * y <= x:
            y += 1
        if y * y > x:
            y -= 1
        return y

sqrtx = SquareRootX()
x = 82
print(sqrtx.mySqrt(x))
