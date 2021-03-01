# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3624/

class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        # manhattan distance
        manh_dist = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        tot_dist, dist = 0, -inf
        for n in nuts:
            tot_dist += manh_dist(n, tree) * 2
            dist = max(dist, manh_dist(n, tree) - manh_dist(n, squirrel))
        return tot_dist - dist

