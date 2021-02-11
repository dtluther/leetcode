# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3630/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        
        result = []
        queue = collections.deque()
        queue.append((root, 0)) # (node, level)
        depth = 0
        last_node = root
        while queue:
            curr, level = queue.popleft()
            if curr.left:
                if 1 + level > depth: # if this is the first time we're seeing this new depth, we can append the las node because it's furthest to the right of the preveious level
                    result.append(last_node.val)
                    depth = 1 + level
                last_node = curr.left
                queue.append((curr.left, 1+level))
            if curr.right:
                if 1 + level > depth: # same here, in case left was null
                    result.append(last_node.val)
                    depth = 1 + level
                queue.append((curr.right, 1+level))
                last_node = curr.right
        result.append(last_node.val)
    
        return result
            
            
