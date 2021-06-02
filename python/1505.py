from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq
import copy

class BIT:
    def lowbit(self, x):
        return x & (-x)

    def __init__(self, n):
        self.n = n
        self.t = [0] * (n+1)

    def add(self, i, x):
        while i <= self.n:
            self.t[i] += x
            i += self.lowbit(i)

    def find(self, i):
        ret = 0
        while i:
            ret += self.t[i]
            i -= self.lowbit(i)

        return ret

    def query(self, l, r):
        return self.find(r) - self.find(l-1)

class Solution:
    def minInteger(self, num: str, k: int) -> str:
        pos = [queue.deque() for _ in range(10)]

        # record the position of elements
        for i, e in enumerate(num):
            pos[ord(e) - ord('0')].append(i+1)
        n = len(num)
        bit = BIT(n)
        ret = []
        for i in range(1, n+1):
            for e in range(10):
                if not pos[e]:
                    continue
                front = pos[e][0]
                # print(e, front)
                cnt = bit.query(front+1, n) + front - i
                if cnt <= k:
                    k -= cnt
                    bit.add(front, 1)
                    pos[e].popleft()
                    ret.append(chr(ord('0') + e))
                    break
        
        return "".join(ret)
        


if __name__ == '__main__':
    sol = Solution()
    s = sol.minInteger(num = "4321", k = 4)
    print(s)
    s = sol.minInteger(num = "100", k = 1)
    print(s)
    s = sol.minInteger("858957035719081", 2)
    print(s)
    s = sol.minInteger("294984148179",11)
    print(s)
