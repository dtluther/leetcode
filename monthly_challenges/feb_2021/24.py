# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/587/week-4-february-22nd-february-28th/3651/

"""
Given a balanced parentheses string S, compute the score of the string based on the following rule:

() has score 1
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.
"""

class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = []
        curr = 0
        for ch in S:
            if ch == '(':
                stack.append(curr)
                curr = 0
            else:
                last = stack.pop()
                curr += last + max(curr, 1)
        return curr
"""
Example 1:

Input: "()"
Output: 1
Example 2:

Input: "(())"
Output: 2
Example 3:

Input: "()()"
Output: 2
Example 4:

Input: "(()(()))"
Output: 6
"""
