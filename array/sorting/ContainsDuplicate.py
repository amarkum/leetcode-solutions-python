"""
https://leetcode.com/problems/contains-duplicate/

217. Contains Duplicate

Given an integer array nums,
return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
"""
from typing import List


class ContainsDuplicate:

    # uses sort
    def containsDuplicateI(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        for i in range(1, len(nums)):
            # check if consecutive elements are repeated after sorting
            if nums[i - 1] == nums[i]:
                return True
        return False

    # uses dict
    def containsDuplicateII(self, nums: List[int]) -> bool:
        maps = {}
        for number in nums:
            if number in maps:
                return True
            else:
                maps.update({number: True})
        return False

    # uses set
    def containsDuplicateIII(self, nums: List[int]) -> bool:
        return False if len(set(nums)) == len(nums) else True


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    contains_duplicate = ContainsDuplicate()
    print(contains_duplicate.containsDuplicateI(nums))
    print(contains_duplicate.containsDuplicateII(nums))
    print(contains_duplicate.containsDuplicateIII(nums))
