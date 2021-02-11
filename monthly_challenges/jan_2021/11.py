# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/580/week-2-january-8th-january-14th/3600/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        """
        nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
        
        [1,2,4,8,9,0,0]
        5
        [3, 6]
        2
        
        can use two pointers with a copy of nums1, and just sort the array
        can use 3 pointers and go in reverse
        
        """
        
        i = m + n - 1
        p1 = m-1
        p2 = n-1
        
        while p1 >= 0 and p2 >= 0:
            print(i, p1, p2)
            v1, v2 = nums1[p1], nums2[p2]
            if v1 > v2:
                nums1[i] = v1
                p1 -= 1
            else:
                nums1[i] = v2
                p2 -= 1
            
            i -= 1
        
        # if any nums left in p2
        nums1[:p2+1] = nums2[:p2+1]
            
        
