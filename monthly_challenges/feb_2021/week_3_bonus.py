# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3640/

class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        from collections import defaultdict, deque

        children = defaultdict(list)
        for parent, child in zip(ppid, pid):
            children[parent].append(child)

        result = []
        queue = deque([kill])
        while queue:
            curr = queue.popleft()
            result.append(curr)

            if curr not in children:
                continue

            for child in children[curr]:
                queue.append(child)

        return result

    """
    n = length of PID (same as PPID)
    Time: O(n), O(n) to build the tree adjacency list, O(n) worst case to build result (if tree is linked list)
    Space: O(n), O(2n) to build tree, O(n) for queue at largest point
    """

"""
Input:
pid =  [1, 3, 10, 5]
ppid = [3, 0, 5, 3]
kill = 5
Output: [5,10]
Explanation:
           3
         /   \
        1     5
             /
            10
Kill 5 will also kill 10.
"""
