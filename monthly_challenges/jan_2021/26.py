# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/582/week-4-january-22nd-january-28th/3617/

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """
        Brute force:
        One option is to DFS and backtrack to find the path of least resistance.

        Pick the next least expensive until we arrive at the end? Djikstras

        Optimal:
        Another option is to pick a resistance threshold, and see if you can get to the end with that threshold.
            If you can, move threshold down (binary search)
            Else, move it up.

        Both would be good options to practice.
        """

        # djikstras variation
        import heapq

        n_rows = len(heights)
        n_cols = len(heights[0])

        differences = [[float('inf') for _ in range(n_cols)] for _ in range(n_rows)]
        differences[0][0] = 0
        visited = [[False for j in range(n_cols)] for i in range(n_rows)]

        queue = [(0, 0, 0)] # difference, x, y
        while queue:
            difference, x, y = heapq.heappop(queue)
            if x == n_rows - 1 and y == n_cols - 1:
                break
            visited[x][y] = True

            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                next_x = x + dx
                next_y = y + dy
                if 0 <= next_x < n_rows and 0 <= next_y < n_cols and not visited[next_x][next_y]:
                    diff = abs(heights[x][y] - heights[next_x][next_y])
                    diff_so_far = max(diff, differences[x][y])

                    if diff_so_far < differences[next_x][next_y]:
                        differences[next_x][next_y] = diff_so_far
                        heapq.heappush(queue, (diff_so_far, next_x, next_y))

        return differences[-1][-1]

