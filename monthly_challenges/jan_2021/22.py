# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/582/week-4-january-22nd-january-28th/3613/

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        counter1 = collections.Counter(word1)
        counter2 = collections.Counter(word2)
        if counter1 == counter2:
            return True
        
        letters1 = set(counter1.keys())
        letters2 = set(counter2.keys())
        count1 = set(counter1.values())
        count2 = set(counter2.values())
        if letters1 == letters2 and count1 == count2:
            return True
        
        return False
