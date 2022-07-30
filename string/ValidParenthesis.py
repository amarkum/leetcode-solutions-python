"""
https://leetcode.com/problems/valid-parentheses/

Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""


class ValidParenthesis:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}
        for char in s:
            if stack and bracket_map.get(char) == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        return not stack


sol = ValidParenthesis()
print(sol.isValid('[{{}()}]'))
