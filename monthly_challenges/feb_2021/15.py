# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3641/

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        """
        Heap
        """
        
#         # 1) min heap of size n
#         import heapq
        
#         heap = []
#         for i, row in enumerate(mat):
#             heapq.heappush(heap, (row.count(1), i))
        
#         return [heapq.heappop(heap)[1] for _ in range(k)]
    
#         """
#         m = rows, n = cols
#         Time: mnlog(m), O(mn) to iterate through the matrix, and heappush is a log(m) operation for the length of the rows
#         Space: O(m)
#         """
        
#         # 2) max heap of size k
#         import heapq
        
#         heap = []
#         for i, row in enumerate(mat):
#             num_soldiers = row.count(1)
#             if len(heap) == k:
#                 heapq.heappushpop(heap, (-num_soldiers, -i)) # negative for max heap
#             else:
#                 heapq.heappush(heap, (-num_soldiers, -i))
        
#         return reversed([-heapq.heappop(heap)[1] for _ in range(k)])
    
#         """
#         Time: mnlog(k), O(mn) to iterate through the heap, and heappush is a log(k) operation for the size of the heap
#         Space: O(k)
#         """
        
        # 3) column interation, move i along and append new entry when we find a new 0 for each row
        rows = []
        added = set()
        for c in range(len(mat[0])):
            for r in range(len(mat)):
                if r in added:
                    continue
                if mat[r][c] == 0:
                    rows.append(r)
                    added.add(r)
                if len(rows) == k:
                    return rows
        
        r = 0
        while len(rows) < k:
            if r not in added:
                rows.append(r)
            r += 1
        
        return rows
    
        """
        Time: O(mn), mn to iterate through matrix + m to iterate through rows again
        Space: O(k) for the extra set
        """

"""
Input: mat =
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]],
k = 3
Output: [2,0,3]
Explanation:
The number of soldiers for each row is:
row 0 -> 2
row 1 -> 4
row 2 -> 1
row 3 -> 2
row 4 -> 5
Rows ordered from the weakest to the strongest are [2,0,3,1,4]

Input: mat =
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]],
k = 2
Output: [0,2]
Explanation:
The number of soldiers for each row is:
row 0 -> 1
row 1 -> 4
row 2 -> 1
row 3 -> 1
Rows ordered from the weakest to the strongest are [0,2,3,1]
"""
