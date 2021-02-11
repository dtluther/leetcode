# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/581/week-3-january-15th-january-21st/3609/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end = None, None
        length = 0
        
        def expand(idx):
            nonlocal length, start, end
        
            # two, one in case they're even, one in case they're odd
            # first case, odd
            i = idx - 1
            j = idx + 1
            l1 = 0
            while i >= 0 and j < len(s):
                if s[i] == s[j]:
                    i -= 1
                    j += 1
                else:
                    break
            l1 = j - i - 1
            
            i2 = idx
            j2 = idx + 1
            while i2 >= 0 and j2 < len(s):
                if s[i2] == s[j2]:
                    i2 -= 1
                    j2 += 1
                else:
                    break
            l2 = j2 - i2 - 1
            
            if l1 > l2:
                if l1 > length:
                    start = i + 1
                    end = j - 1
                    length = l1
            elif l2 > length:
                start = i2 + 1
                end = j2 - 1
                length = l2
                    
        for i in range(len(s)):
            expand(i)
        
        return s[start:end+1] if end else s[0]
