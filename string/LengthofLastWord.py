"""
https://leetcode.com/problems/length-of-last-word/

Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
"""
class LengthofLastWord:
    def lengthOfLastWord(self, s: str) -> int:
        parts = s.split()
        return len(parts[-1])


Length_of_last_word = LengthofLastWord()
s = "   fly me   to   the moon  "

print(Length_of_last_word.lengthOfLastWord(s))
