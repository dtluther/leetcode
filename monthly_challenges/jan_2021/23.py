# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/582/week-4-january-22nd-january-28th/3614/

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        def diag_sort(row, col):
            nums = []
            
            i, j = row, col
            while i < len(mat) and j < len(mat[0]):
                nums.append(mat[i][j])
                i += 1
                j += 1
            
            # # not sure why this isn't faster than the sort below
            # heapq.heapify(nums)
            # while nums:
            #     mat[row][col] = heapq.heappop(nums)
            #     row += 1
            #     col += 1
                
            nums.sort(reverse=True)
            while nums:
                mat[row][col] = nums.pop()
                row += 1
                col += 1
                
        for i in range(len(mat)):
            diag_sort(i, 0)
        
        for j in range(1, len(mat[0])):
            diag_sort(0, j)
        
        return mat
