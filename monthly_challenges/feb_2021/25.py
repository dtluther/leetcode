# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/587/week-4-february-22nd-february-28th/3652/

"""
Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

Return the shortest such subarray and output its length.

Constraints:

1 <= nums.length <= 104
-105 <= nums[i] <= 105


Follow up: Can you solve it in O(n) time complexity?
"""

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
#         # n log n
#         s = sorted(nums)
#         first = -1
#         last = -1
#         for i, val in enumerate(s):
#             if val != nums[i]:
#                 first = i
#                 break
#         for i in range(len(s)-1, -1, -1):
#             if s[i] != nums[i]:
#                 last = i
#                 break
        
#         if first > -1 and last > -1:
#             return last - first + 1
#         return 0

        # O(n), 4 iterations placing the min and the max correctly
        found_peak = False
        min_after = float('inf')

        for i in range(1, len(nums)):
            val = nums[i]
            if val < nums[i-1]:
                found_peak = True
            if found_peak:
                min_after = min(val, min_after)
        
        if not found_peak:
            return 0
        
        
        for i, val in enumerate(nums):
            if min_after < val:
                start = i
                break
        
        found_valley = False
        max_after = float('-inf')
        for j in range(len(nums)-2, -1, -1):
            val = nums[j]
            if val > nums[j+1]:
                found_valley = True
            if found_valley:
                max_after = max(val, max_after)
        
        for j in range(len(nums)-1, -1, -1):
            val = nums[j]
            if max_after > val:
                end = j
                break
        
        return end - start + 1

"""
Example 1:

Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Example 2:

Input: nums = [1,2,3,4]
Output: 0
Example 3:

Input: nums = [1]
Output: 0
"""
