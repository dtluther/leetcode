# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/581/week-3-january-15th-january-21st/3611/

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        """
        use stack, notes in paper pro
        """
        
        stack = [nums[0]]
        for i in range(1, len(nums)):
            remaining = len(nums) - i
            val = nums[i]
            while stack and val < stack[-1] and remaining + len(stack) > k:
                stack.pop()
            stack.append(val)
        
        return stack[:k]
