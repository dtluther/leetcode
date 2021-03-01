# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/587/week-4-february-22nd-february-28th/3655/

class FreqStack:
    # stack of stacks
    def __init__(self):
        self.count = collections.Counter()
        self.count_groups = collections.defaultdict(list)
        self.max_count = 0

    def push(self, x: int) -> None:
        self.count[x] += 1
        if self.count[x] > self.max_count:
            self.max_count = self.count[x]
        self.count_groups[self.count[x]].append(x)

    def pop(self) -> int:
        x = self.count_groups[self.max_count].pop()
        self.count[x] -= 1
        if not self.count_groups[self.max_count]:
            self.max_count -= 1
    
        return x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
