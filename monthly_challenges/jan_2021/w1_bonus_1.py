# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3588/
# Palindrome Permutation

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        from collections import defaultdict
        ch_count = defaultdict(int)
        
        for ch in s:
            ch_count[ch] += 1
        
        odds = 0
        for count in ch_count.values():
            if count % 2 != 0:
                odds += 1
            if odds > 1:
                return False
        
        return True
