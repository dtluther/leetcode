# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/582/week-4-january-22nd-january-28th/3619/

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        from string import ascii_lowercase
        alph_map = dict(zip(range(1, 27), ascii_lowercase))
        
        result = ""
        while k > n:
            if k - n >= 26:
                val = 26
            else:
                val = k - n + 1
                
            k -= val
            result = alph_map[val] + result
            n -= 1
            
        result = 'a' * n + result
        
        return result
