# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3644/

class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0

        last = A[1] - A[0]
        digit_streak = 2
        count = 0
        for i in range(2, len(A)):
            num = A[i]
            prev = A[i-1]
            if num - prev == last:
                digit_streak += 1
                count += (digit_streak - 2)
            else:
                digit_streak = 2
                last = num - prev

        return count

"""
Input: [1,2,3,4]
Output: 3

Input: [1,2,3,4,5]
Output: 6

Input: [1,2,3,4,5,6]
Output: 10

[1,4,5,6,7]
Output: 3
"""
