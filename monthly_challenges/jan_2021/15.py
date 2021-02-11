# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/581/week-3-january-15th-january-21st/3605/

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        arr = [0 for i in range(n+1)]
        arr[0] = 0
        arr[1] = 1
        for i in range(2, n+1):
            if i % 2 == 0:
                arr[i] = arr[i//2]
            else:
                half = (i-1) // 2
                arr[i] = arr[half] + arr[half+1]
        
        return max(arr)
