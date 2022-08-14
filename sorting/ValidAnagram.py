"""
https://leetcode.com/problems/valid-anagram/

242. Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
"""


class ValidAnagram:
    def isAnagramI(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    def isAnagramII(self, s: str, t: str) -> bool:
        from collections import Counter
        return Counter(s) == Counter(t)


s = "anagram"
t = "nagaram"

valid_anagram = ValidAnagram()
print(valid_anagram.isAnagramI(s, t))
print(valid_anagram.isAnagramII(s, t))
