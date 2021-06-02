from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        cnt = collections.Counter(s)
        stack = []
        n = len(s)
        for i in range(n):
            cnt[s[i]] -= 1
            if s[i] in stack:
                continue
            while stack and stack[-1] > s[i] and cnt[stack[-1]] > 0:
                stack.pop()

            stack.append(s[i])

        return "".join(stack)


if __name__ == '__main__':
    sol = Solution()
    s = sol.removeDuplicateLetters("cbacdcbc")
    print(s)
    s = sol.removeDuplicateLetters("bcabc")
    print(s)