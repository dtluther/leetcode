# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/587/week-4-february-22nd-february-28th/3649/

class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        def is_subsequence(word):
            i = 0
            j = 0
            
            while i < len(s) and j < len(word):
                if s[i] == word[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            
            return j == len(word)
        
        long = ""
        for w in d:
            if is_subsequence(w):
                if len(w) > len(long):
                    long = w
                elif len(w) == len(long):
                    long = min(w, long)
            
        return long

"""
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output:
"apple"

Input:
s = "abpcplea", d = ["a","b","c"]

Output:
"a"
"""
