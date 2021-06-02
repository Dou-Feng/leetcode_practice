from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq
import copy
import random

class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        # 广搜
        n = len(row) // 2
        g = [[] for _ in range(n)]
        for i in range(n):
            l, r = row[i*2] // 2, row[i*2+1] // 2
            if l != r:
                g[l].append(r)
                g[r].append(l)

        ret = 0
        visited = [False] * n
        for e in range(n):
            if visited[e]:
                continue
            cnt = 1
            q = queue.deque()
            q.append(e)
            visited[e] = True
            while q:
                f = q.popleft()
                for node in g[f]:
                    if not visited[node]:
                        q.append(node)
                        cnt += 1
                        visited[node] = True
            ret += cnt - 1

        return ret

def swap(l, i, j):  
    t = l[i]
    l[i] = l[j]
    l[j] = t


if __name__ == '__main__':

    sol = Solution()
    n = 60
    row = [i for i in range(0, n)]
    for _ in range(100):
        i = random.randint(0, n-1)
        j = random.randint(0, n-1)
        swap(row, i, j)

    print(row)
    s = sol.minSwapsCouples(row)
    print(s)