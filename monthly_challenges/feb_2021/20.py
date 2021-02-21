# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3646/

class Solution:
    def romanToInt(self, s: str) -> int:
        if not s:
            return 0
        
        digit = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        last = digit[s[-1]]
        result = last
        for i in range(len(s)-2, -1, -1):
            value = digit[s[i]]
            if value < last:
                result -= value
            else:
                result += value
                last = value
        
        return result
    # Time: O(n)
    # Space: O(1), same space for map, result, and last

"""
Input: s = "III"
Output: 3

Input: s = "IV"
Output: 4

Input: s = "IX"
Output: 9

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""
