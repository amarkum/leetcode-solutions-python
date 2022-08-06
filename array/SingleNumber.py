"""
https://leetcode.com/problems/single-number/

136. Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:

Input: nums = [2,2,1]
Output: 1
"""

from typing import List


class SingleNumber:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            if num in dic:
                dic.update({num: dic.get(num) + 1})
            else:
                dic.update({num: 1})
        for key, value in dic.items():
            if value == 1:
                return key


nums = [1, 2, 3, 4, 2, 4, 3]
single_number = SingleNumber()
print(single_number.singleNumber(nums))
