# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/585/week-2-february-8th-february-14th/3638/

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0:
            return -1
            
        from collections import deque
        
        size = len(grid)
        # dirs = [(0,1), (1,0), (0,-1), (-1, 0)]
        
        queue = deque() # dist, x, y
        queue.append((1,0,0))
        visited = set()
        visited.add((0,0))
        while queue:
            dist, x, y = queue.popleft()
            
            if x == size-1 and y == size-1:
                return dist
            
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    rx, ry = x + dx, y + dy
                    if (rx,ry) not in visited and 0 <= rx < size and 0 <= ry < size and grid[rx][ry] == 0:
                        queue.append((1+dist, rx, ry))
                        visited.add((rx, ry))
        
        return -1

"""
Input: [[0,1],[1,0]]
Output: 2

Input: [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
"""

