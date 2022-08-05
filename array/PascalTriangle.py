"""
https://leetcode.com/problems/pascals-triangle/

118. Pascal's Triangle

Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
"""

from typing import List


class PascalTriangle:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1], [1, 1]]
        # build pascal series from 3 onwards
        if numRows > 2:
            for i in range(2, numRows):
                # first and last of the pascal series i '1'
                entry = [0] * (i + 1)
                entry[0] = entry[i] = 1

                # add up val(current index + next index) from prev pascal number to fill in
                for k in range(0, len(pascal[i - 1]) - 1):
                    entry[k + 1] = pascal[i - 1][k] + pascal[i - 1][k + 1]

                # add the pascal entry
                pascal.append(entry)

        # return unto n pascal series
        return pascal[:numRows]
