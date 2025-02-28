"""
231. Power of Two
https://leetcode.com/problems/power-of-two/description/

Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2x.

Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1
Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16
Example 3:

Input: n = 3
Output: false

"""

class TwoPairs(object):
    def isPowerOfTwo(self, n):
        return n > 0 and (n & (n - 1)) == 0

if __name__ == '__main__':
    number = 16
    two_pairs = TwoPairs()
    print(two_pairs.isPowerOfTwo(number))
