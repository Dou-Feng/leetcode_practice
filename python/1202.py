from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq

## 高度较低的并查集
class UF_balanced:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.depth = [1] * n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xp, yp = self.find(x), self.find(y)

        if xp == yp:
            return False

        ## union
        if self.depth[xp] < self.depth[yp]:
            t = xp
            xp = yp
            yp = t
        self.parent[xp] = self.parent[yp]
        self.depth[xp] += self.depth[yp]

        return True

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        uf = UF_balanced(n)
        for pair in pairs:
            a, b = pair[0], pair[1]
            uf.union(a, b)

        grps = collections.defaultdict(list)
        for i in range(n):
            # grps[uf.find(i)].append(i)
            # use heap
            heapq.heappush(grps[uf.find(i)], s[i])

        ans = []
        for i in range(n):
            ans.append( heapq.heappop(grps[uf.find(i)]) )

        return "".join(ans)


if __name__ == '__main__':
    sol = Solution()
    s = sol.smallestStringWithSwaps(s = "dcab", pairs = [[0,3],[1,2]])
    print(s)
    s = sol.smallestStringWithSwaps(s = "dcab", pairs = [[0,3],[1,2],[0,2]])
    print(s)
    s = sol.smallestStringWithSwaps(s = "cba", pairs = [[0,1],[1,2]])
    print(s)