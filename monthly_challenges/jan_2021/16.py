# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/581/week-3-january-15th-january-21st/3606/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Quickselect: Quicksort mixed with binary search
        1. Pick pivot
        2. Put the pivot in the correct spot
            If the spot is k, return el
            elif k > pivot:
                repeat on right side
            else:
                repeat on left side
                
        quicksort in place
        [3,4,1,5,2]
        | <- wall
        pivot=3
        if num is less, swap with pivot and move wall
        [3,1,4,5,2]
          |
        [3,1,2,5,4]
            |
                
        """
        result = None
        def quickselect(i=0, j=len(nums)-1):
            nonlocal result
            
            pivot_idx = i
            wall = i
            for idx in range(i, j+1):
                val = nums[idx]
                if val > nums[pivot_idx]:
                    wall += 1
                    nums[wall], nums[idx] = nums[idx], nums[wall]
            # swap end of wall with pivot
            nums[pivot_idx], nums[wall] = nums[wall], nums[pivot_idx]
            if wall + 1 == k:
                result = nums[wall]
                return
            elif k < wall + 1:
                quickselect(pivot_idx, wall-1)
            else:
                quickselect(wall+1, len(nums)-1)
        
        quickselect()
        return result
