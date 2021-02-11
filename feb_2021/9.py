# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/585/week-2-february-8th-february-14th/3634/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Topsort
        2 ways
        Kahn's Algo
        Post order DFS, reversed
        """

        # 1) Kahn's algorithm (using indegrees)
        graph = defaultdict(list)
        indegrees = [0] * numCourses
        for pre, course in prerequisites:
            graph[pre].append(course)
            indegrees[course] += 1

        queue = deque()
        for i, count in enumerate(indegrees):
            if count == 0:
                queue.append(i)

        result = []
        while queue:
            curr = queue.popleft()
            result.append(curr)

            for desc in graph[curr]:
                indegrees[desc] -= 1
                if indegrees[desc] == 0:
                    queue.append(desc)

        return len(result) == numCourses

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        """
        DFS
        
                    5
                /       \
               3         7  total = 8
            /   \       /   \
           2     4     6     8
           
                    20
                /       \
               27         15
            /   \           \
           29     24            8
        
        If right:
            greater = dfs(right)
            node.val = node.val + greater
        if left:
            node.left.val = node.val + node.left.val
            dfs(node.left)
        
        return node.val
        """
        
        # with nonlocal variable
#         total = 0
#         def reverse_order(node):
#             nonlocal total
#             if not node:
#                 return
            
#             reverse_order(node.right)
#             total += node.val
#             node.val = total
#             reverse_order(node.left)
        
#         reverse_order(root)
#         return root

        def reverse_order(node, path_sum=0):
            if not node:
                return path_sum
            
            right = reverse_order(node.right, path_sum)
            node.val += right
            left = reverse_order(node.left, node.val)
            return left
        
        reverse_order(root)
        return root
