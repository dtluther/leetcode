# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/585/week-2-february-8th-february-14th/3632/

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        
        def search_island(x, y):
            if not (0 <= x < rows and 0 <= y < cols): return
            
            if (x,y) in seen: return
            
            seen.add((x,y))
            if not grid[x][y]:
                return
            
            island.add((x-row_org,y-col_org))
            for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                search_island(x+dx, y+dy)
            
        rows = len(grid)
        cols = len(grid[0])
        
        seen = set()
        uniq_islands = set()
        for r in range(rows):
            for c in range(cols):
                island = set()
                row_org = r
                col_org = c
                search_island(r, c)
                if island:
                    uniq_islands.add(frozenset(island))
        
        return len(uniq_islands)
                    
"""
Example 1:
11000
11000
00011
00011
Given the above grid map, return 1.

Example 2:
11011
10000
00001
11011
Given the above grid map, return 3.

Notice that:
11
1
and
 1
11
are considered different island shapes, because we do not consider reflection / rotation.
"""
