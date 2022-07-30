import collections
from typing import List

"""
https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/

Least Number of Unique Integers after K Removals
Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.


Input: arr = [5,5,4], k = 1
Output: 1
Explanation: Remove the single 4, only 5 is left.
"""


class LeastNumberKRemoval:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        map = collections.defaultdict(int)
        for num in arr:
            map[num] = map.get(num, 0) + 1

        sorted_map = dict(sorted(map.items(), key=lambda e: e[1]))

        counter = 0
        for key, val in sorted_map.items():
            if k >= val:
                k -= val
                counter += 1
            if k < 0:
                break

        return len(sorted_map) - counter

    def findLeastNumOfUniqueIntsAlternate(self, arr: List[int], k: int) -> int:
        # map = {element: arr.count(element) for element in arr}
        map = collections.defaultdict(int)
        for num in arr:
            map[num] = map.get(num, 0) + 1
        sorted_map = dict(sorted(map.items(), key=lambda e: e[1]))
        counter = 0
        removed = 0
        for key, value in sorted_map.items():
            for decrementing_value in range(value):
                if counter == k:
                    break
                if sorted_map.get(key) > 0:
                    value -= 1
                    sorted_map.update({key: value})
                    counter += 1
                if sorted_map.get(key) == 0:
                    removed += 1
        return len(sorted_map) - removed


least_number_after_k = LeastNumberKRemoval()
arr = [4, 3, 1, 1, 3, 3, 2]
k = 2
print(least_number_after_k.findLeastNumOfUniqueInts(arr, k))
print(least_number_after_k.findLeastNumOfUniqueIntsAlternate(arr, k))
