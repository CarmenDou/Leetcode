# 这道题用队列，有一个思路就是判断每一个beginword换一个字母之后是不是在wordlist里。 如果这个新的单词等于endword，那么循环结束，返还step的次数。
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        queue =deque([beginWord])
        step,l = 0,len(beginWord)
        while queue:
            step += 1
            size = len(queue)
            while size:
                cur = queue.popleft()
                for i in range(l):
                    for char in "abcdefghijklmnopqrstuvwxyz":
                        new = cur[:i] + char + cur[i+1:]

                        if new not in wordSet:
                            continue

                        if new == endWord:
                            return step + 1

                        queue.append(new)
                        wordSet.discard(new)
                size -= 1
             
        return 0
```