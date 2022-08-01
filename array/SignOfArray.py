"""
1822. Sign of the Product of an Array
There is a function signFunc(x) that returns:

1 if x is positive.
-1 if x is negative.
0 if x is equal to 0.
You are given an integer array nums. Let product be the product of all values in the array nums.

Return signFunc(product).
"""

from typing import List


class SignOfArray:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        product = 1
        for num in nums:
            product *= num
        return 1 if product > 1 else -1


sign_of_array = SignOfArray()
nums = [-1, -2, -3, -4, 3, 2, 1]
print(sign_of_array.arraySign(nums))
