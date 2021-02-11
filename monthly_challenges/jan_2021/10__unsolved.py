"""
https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/580/week-2-january-8th-january-14th/3599/
"""

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        if not instructions:
            return 0
        
        cost = 0
        s = [instructions[0]]
        minimum = s[0]
        maximum = s[0]
        for val in instructions[1:]:
            if val <= minimum:
                s = [val] + s
                minimum = val
            elif val >= maximum:
                s.append(val)
                maximum = val
            else:
                for idx, num in enumerate(s):
                    if val < num:
                        cost += min(idx, len(s)-idx)
                        s.insert(idx, val)
                        break
                    elif val == num:
                        for r_idx, n in enumerate(reversed(s)):
                            if n == val:
                                rev_idx = r_idx
                        last_idx = len(s) - rev_idx - 1
                        left_min = min(idx, len(s)-idx)
                        right_min = min(last_idx+1, len(s)-(last_idx+1))
                        print(last_idx)
                        print(s)
                        print(val)
                        print(left_min, right_min)
                        if left_min <= right_min:
                            cost += left_min
                            s.insert(idx, val)
                        else:
                            cost += right_min
                            s.insert(last_idx+1, val)
                        break
                        
                        
#                 # binary search
#                 start = 0
#                 stop = len(s)-1
#                 while start < stop:
#                     mid = (start+stop) // 2
#                     print(s, val)
#                     print(mid)
#                     if s[mid] <= val < s[mid+1]:
#                         cost += min(len(s)-(mid+1), mid+1)
#                         print('right', cost)
#                         print(cost)
#                         s.insert(mid+1, val)
#                         break
#                     elif s[mid-1] < val <= s[mid]:
#                         cost += min(len(s)-mid, mid)
#                         print('left', cost)
#                         s.insert(mid, val)
#                         break
#                     elif val > s[mid]:
#                         start = mid+1
#                     elif val < s[mid]:
#                         stop = mid-1
                    
#                     if start == len(s) - 1:
#                         s.append(val)
#                     elif stop == 0:
#                         s = [val] + s
        
        return cost
                    
            
