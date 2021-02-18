# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3643/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) <= 1:
            return 0
        
        max_area = 0
        i = 0
        j = len(height) - 1
        while i < j:
            area = min(height[i], height[j]) * (j - i)
            max_area = max(area, max_area)
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        
        return max_area
