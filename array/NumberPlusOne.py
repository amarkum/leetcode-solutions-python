"""
https://leetcode.com/problems/plus-one/

66. Plus One

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
"""

from typing import List


class NumberPlusOne:
    def plusOne(self, digits: List[int]) -> List[int]:
        if all(x == 9 for x in digits):
            digits[0] = 1
            for i in range(1, len(digits)):
                digits[i] = 0
            digits.append(0)
        elif digits[-1] == 9:
            for i in range(len(digits)):
                if digits[-(i + 1)] != 9:
                    digits[-(i + 1)] = digits[-(i + 1)] + 1
                    break
                else:
                    digits[-(i + 1)] = 0
        else:
            digits[-1] = digits[-1] + 1
        return digits


number = [1, 2, 3]
number_plus_one = NumberPlusOne()
print(number_plus_one.plusOne(number))
