"""
163. Missing Ranges

You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are within the inclusive range.
A number x is considered missing if x is in the range [lower, upper] and x is not in nums.
Return the shortest sorted list of ranges that exactly covers all the missing numbers. That is, no element of nums is included in any of the ranges, and each missing number is covered by one of the ranges.

Example 1:

Input: nums = [0,1,3,50,75], lower = 0, upper = 99
Output: [[2,2],[4,49],[51,74],[76,99]]
Explanation: The ranges are:
[2,2]
[4,49]
[51,74]
[76,99]
Example 2:

Input: nums = [-1], lower = -1, upper = -1
Output: []
Explanation: There are no missing ranges since there are no missing numbers.

"""

class MissingRanges(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[List[int]]
        """
        if not nums:
            return [[lower, upper]]

        main_list = []

        if lower < nums[0]:
            main_list.append([lower, nums[0] - 1])

        for i in range(len(nums) - 1):
            diff = nums[i + 1] - nums[i]
            if diff > 1:
                a = nums[i] + 1
                b = nums[i + 1] - 1
                main_list.append([a, b])

        if upper > nums[-1]:
            main_list.append([nums[-1] + 1, upper])

        return main_list


if __name__ == '__main__':
    nums = [0, 1, 12]
    upper = 0
    lower = 9
    missing_ranges = MissingRanges()
    print(missing_ranges.findMissingRanges(nums, lower, upper))
