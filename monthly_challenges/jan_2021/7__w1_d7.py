# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3595/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        abcabcbb
        Use a moving window
        {a:1, b:1, c:1}
        Once I hit a again, value goes to 2
        iterate my front pointer until a is at 1 again
        Repeat this through the end
        """
                
        from collections import defaultdict
        slow = 0
        fast = 0
        long = 0
        ch_count = defaultdict(int)
        
        while fast < len(s):
            fast_ch = s[fast]
            ch_count[fast_ch] += 1
            fast += 1
            
            while ch_count[fast_ch] > 1:
                slow_ch = s[slow]
                ch_count[slow_ch] -= 1
                slow += 1
                
            long = max(long, fast-slow)
        
        return long        
