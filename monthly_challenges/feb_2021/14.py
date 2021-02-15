# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/585/week-2-february-8th-february-14th/3639/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        from collections import deque
        
        TEAM1 = 'A'
        TEAM2 = 'B'
        seen = {}
        queue = deque()
        for i in range(len(graph)):
            if i not in seen:
                seen[i] = TEAM1
                queue.append(i)
            while queue:
                curr = queue.popleft()
                team = seen[curr]
                other_team = TEAM1 if team == TEAM2 else TEAM2
                
                for nei in graph[curr]:
                    if nei in seen:
                        if seen[nei] == team:
                            return False
                        else:
                            continue
                    queue.append(nei)
                    seen[nei] = other_team
        
        return True

"""
Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: false
Explanation: There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.

Input: graph = [[1,3],[0,2],[1,3],[0,2]]
Output: true
Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.
"""
