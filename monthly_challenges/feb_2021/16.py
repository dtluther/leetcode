# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3642/

"""
Learned some great things here:
    1) str`.isalpha()` returns `True` if all chars in the string are alphabetic, and there is at least one character.
    2) str`.swapcase()` swaps the case of every alphabetic char in the string.
    3. Great demonstration of recursion. The pic posted here is very helpful: https://leetcode.com/problems/letter-case-permutation/discuss/379928/Python-clear-solution
"""

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        result = []
        
        def build_string(sub="", idx=0):
            if len(sub) == len(S):
                result.append(sub)
                return
            
            if S[idx].isalpha():
                build_string(sub + S[idx].swapcase(), idx+1)
            build_string(sub + S[idx], idx+1)
        
        build_string()
        return result
                
"""
Input: S = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]

Input: S = "3z4"
Output: ["3z4","3Z4"]

Input: S = "12345"
Output: ["12345"]

Input: S = "0"
Output: ["0"]
"""
