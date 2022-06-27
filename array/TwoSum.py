class TwoSum(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            required_number = target - nums[i]
            for j in range(i + 1, len(nums)):
                if required_number == nums[j]:
                    return [i, j]
