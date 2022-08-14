"""
https://leetcode.com/problems/third-maximum-number/submissions/

414. Third Maximum Number

Given an integer array nums, return the third distinct maximum number in this array.
If the third maximum does not exist, return the maximum number.

Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
"""
from typing import List


class ThirdMaximum:
    def thirdMax(self, nums: List[int]) -> int:
        sorted_nums = sorted(set(nums))
        if len(sorted_nums) < 3:
            return max(sorted_nums)
        return sorted_nums[-3]


if __name__ == '__main__':
    nums = [3, 2, 1]
    third_maximum = ThirdMaximum()
    print(third_maximum.thirdMax(nums))
