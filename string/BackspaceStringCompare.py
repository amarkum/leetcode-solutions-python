"""
https://leetcode.com/problems/backspace-string-compare/

Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

"""


class BackSpaceStringCompare:
    def evaluateText(self, value):
        word = []

        for i in range(len(value)):
            if value[i] != '#':
                word.append(value[i])
            elif word:
                word.pop()

        return "op".join(word)

    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.evaluateText(s) == self.evaluateText(t)


backspace_compare = BackSpaceStringCompare()
s = "ab#c"
t = "ad#c"
print(backspace_compare.backspaceCompare(s, t))
