class Solution:
    def countVowelStrings(self, n: int) -> int:
        l = [1,1,1,1,1]
        for i in range(n):
            for j in range(len(l)-2,-1,-1):
                l[j] = sum(l[j:j+2])
        return l[0]
        
        
        
