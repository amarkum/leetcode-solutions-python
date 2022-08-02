"""
https://leetcode.com/problems/add-binary/

67. Add Binary
Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"
"""


class AddBinaryNumbers:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


a = "11"
b = "1"
add_binary_numbers = AddBinaryNumbers()
print(add_binary_numbers.addBinary(a, b))
