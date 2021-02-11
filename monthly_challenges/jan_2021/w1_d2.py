# https://leetcode.com/explore/featured/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3590/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        """
        BFS cloned, check if node is target
        """


        queue1 = [original]
        queue2 = [cloned]
        while queue1:
            curr1 = queue1.pop(0)
            curr2 = queue2.pop(0)
            if curr1 == target:
                return curr2
            if curr1.left:
                queue1.append(curr1.left)
                queue2.append(curr2.left)
            if curr1.right:
                queue1.append(curr1.right)
                queue2.append(curr2.right)
