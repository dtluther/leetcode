# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3629/

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        curr = ''
        for ch in path:
            if ch == '/' and curr:
                if curr not in ['.', '..']:
                    stack.append(curr)
                elif curr == '..':
                    if stack:
                        stack.pop()
                curr = ''
            elif ch == '/':
                continue
            else:
                curr += ch
        
        if curr:
            if curr not in ['.', '..']:
                stack.append(curr)
            elif curr == '..':
                if stack:
                    stack.pop()
        
        print(stack)
        result = "/".join(stack)
        return f"/{result}"
