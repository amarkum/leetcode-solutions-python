"""
https://leetcode.com/problems/majority-element/

169. Majority Element

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.


Example 1:

Input: nums = [3,2,3]
Output: 3
"""
from typing import List


class MajorityElement:
    def majorityElement(self, nums: List[int]) -> int:
        majority = len(nums) / 2
        from collections import defaultdict
        maps = defaultdict(int)
        for i in nums:
            maps[i] = maps.get(i, 0) + 1
        for k, v in dict(maps).items():
            if v > majority:
                return k


nums = [3, 2, 3]
majority_element = MajorityElement()
print(majority_element.majorityElement(nums))
