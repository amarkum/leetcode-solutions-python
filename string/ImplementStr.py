"""
https://leetcode.com/problems/implement-strstr/

28. Implement strStr()
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

"""


class ImplementStr:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if needle in haystack:
            return haystack.find(needle)
        else:
            return -1


haystack = "hello"
needle = "ll"
implement_str = ImplementStr()
print(implement_str.strStr(haystack, needle))
