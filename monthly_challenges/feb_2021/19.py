# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3645/

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []

        chars = list(s)
        i = 0
        while i < len(chars):
            ch = chars[i]
            if ch == '(':
                stack.append(ch)
            elif ch == ')':
                if not stack:
                    chars.pop(i)
                    i -= 1
                else:
                    stack.pop()
            i += 1

        stack = []
        j = len(chars) - 1
        while j >= 0:
            ch = chars[j]
            if ch == ')':
                stack.append(ch)
            elif ch == '(':
                if not stack:
                    chars.pop(j)
                else:
                    stack.pop()
            j -= 1

        return "".join(chars)

    """
    Time: O(n) for 2 linear passes
    Space: O(n) if the whole string is one type of paren
    """

"""
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Input: s = "a)b(c)d"
Output: "ab(c)d"

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.

Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"
"""
