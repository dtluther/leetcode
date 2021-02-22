# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3647/

class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        """
        Can work backwards, and divide by 2 whenever it's an option
        """
        
        result = 0
        while Y > X:
            if Y % 2 != 0:
                Y += 1
            else:
                Y //= 2
                
            result += 1

        return result + (X-Y) # this will get us the further decrements

"""
Input: X = 2, Y = 3
Output: 2
Explanation: Use double operation and then decrement operation {2 -> 4 -> 3}.

Input: X = 5, Y = 8
Output: 2
Explanation: Use decrement and then double {5 -> 4 -> 8}.

Input: X = 3, Y = 10
Output: 3
Explanation:  Use double, decrement and double {3 -> 6 -> 5 -> 10}.

Input: X = 1024, Y = 1
Output: 1023
Explanation: Use decrement operations 1023 times.
"""
