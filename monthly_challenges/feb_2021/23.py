# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/587/week-4-february-22nd-february-28th/3650/

"""
Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        1   4  7 11 15
        2   5  8 12 19
        3   6  9 16 22
        10 13 14 17 24
        18 21 23 26 30
        
        1. Start bottom left corner
        2. compare
            return True if val == target
            if target is < val
                we can move up a row because we know it can't be in the current row because all values to the right are greater
            if target is > val
                we can move a column to the right because we know we don't need to check the value above us because it's less than the current value
        3. we repeat this until we hit the target or go out of bounds
        
        """
        if not matrix:
            return False
        
        r = len(matrix) - 1
        c = 0
        
        while 0 <= r < len(matrix) and 0 <= c < len(matrix[0]):
            val = matrix[r][c]
            if target == val:
                return True
            if target < val:
                r -= 1
            else:
                c += 1
            
        return False
        
    """
    m = rows, n = cols
    Time: O(m + n), because worst case scenario is it goes through an entire row and up an entire column and doesn't find the value
    Space: O(1), just some variables that hold values (like r, c, etc.)
    """

"""
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true

Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false
"""
        
