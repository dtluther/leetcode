# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3626/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        def trim(node):
            if not node:
                return
            
            if node.val < low:
                return trim(node.right)
            if node.val > high:
                return trim(node.left)
            
            node.left = trim(node.left)
            node.right = trim(node.right)
            
            return node
        
        return trim(root)
