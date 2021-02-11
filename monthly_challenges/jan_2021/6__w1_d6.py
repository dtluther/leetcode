# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3594/

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        """
        [2,3,4,7,11], k = 5
        
        """
        if not arr:
            return k
        
        count = 0 # 2 @ 5, 3 @ 6, 4 @ 8, 5 @ 9
        result = None
        
        j = 0
        i = 1
        while True:
            # if index in array and value matches
            if j < len(arr) and arr[j] == i:
                j += 1
            else:
                count += 1
            if count == k:
                result = i
                break
            i += 1
                
        return result
