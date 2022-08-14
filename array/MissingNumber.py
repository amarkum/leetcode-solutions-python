"""
https://leetcode.com/problems/missing-number/

268. Missing Number
Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.

Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3].
2 is the missing number in the range since it does not appear in nums.
"""
from typing import List


class MissingNumber:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        partial_sum = n * (n + 1) // 2
        return abs(total - partial_sum)


if __name__ == '__main__':
    nums = [3, 0, 1]
    missing_number = MissingNumber()
    print(missing_number.missingNumber(nums))
