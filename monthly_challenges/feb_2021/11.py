# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/585/week-2-february-8th-february-14th/3636/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        s_count = Counter(s)
        for ch in t:
            if ch not in s_count:
                return False
            if s_count[ch] == 0:
                return False
            s_count[ch] -= 1
        
        return True
    
    # Time: O(m + n)
    # Sapce: O(1) since the max space would be 26 letters
