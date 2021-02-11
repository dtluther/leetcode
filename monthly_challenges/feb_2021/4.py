# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3628/

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        if len(counts) <= 1:
            return 0

        long = 0
        for num in counts:
            total = counts[num]
            if num - 1 in counts and num + 1 in counts:
                total += max(counts[num-1], counts[num+1])
            elif num - 1 in counts:
                total += counts[num-1]
            elif num + 1 in counts:
                total += counts[num+1]
            else:
                total = 0
            
            long = max(total, long)
            
        
        return long
            
