# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/580/week-2-january-8th-january-14th/3598/

# The legendary word ladder

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import deque
        from string import ascii_lowercase

        if endWord not in wordList:
            return 0

        s = set(wordList)
        s.discard(beginWord)
        queue = deque()
        queue.append(beginWord)

        level = 1
        while queue:
            level += 1
            for i in range(len(queue)):
                letters = list(queue.popleft())
                for j in range(len(letters)):
                    temp = letters[j]
                    for ch in ascii_lowercase:
                        letters[j] = ch
                        word = "".join(letters)
                        if word in s:
                            if word == endWord:
                                return level
                            queue.append(word)
                            # print('the current word', word)
                            # print(s)
                            s.remove(word)
                    letters[j] = temp

        return 0
