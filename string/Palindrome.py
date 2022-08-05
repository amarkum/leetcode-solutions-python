"""
125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
"""


class Palindrome:
    def isPalindrome(self, s: str) -> bool:
        text = "".join([x for x in s if x.isalnum()]).lower()
        return text == text[::-1]


s = "A man, a plan, a canal: Panama"
palindrome = Palindrome()
print(palindrome.isPalindrome(s))
