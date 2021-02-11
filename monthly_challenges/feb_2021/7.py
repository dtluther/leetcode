# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3631/

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        """
        iterate both directions and take min from last
        """
        prev = float('-inf')
        result = []
        for i, ch in enumerate(s):
            if ch == c:
                prev = i
            result.append(i - prev)

        prev = float('inf')
        for i in range(len(s)-1, -1, -1):
            if s[i] == c:
                prev = i
            result[i] = min(result[i], prev - i)

        return result
