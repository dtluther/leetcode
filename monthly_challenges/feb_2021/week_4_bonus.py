# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/587/week-4-february-22nd-february-28th/3648/

# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        def is_celebrity(i):
            for j in range(n):
                if i == j: continue
                if knows(i, j) or not knows(j, i):
                    return False
            return True

        for i in range(n):
            if is_celebrity(i):
                return i
        return -1

