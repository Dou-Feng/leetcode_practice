from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq
import copy

class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        n, mod = len(hats), 10**9 + 7
        maxHatId = max(max(ids) for ids in hats)
        f = [[0] * (1 << n) for _ in range(maxHatId+1)]
        
        
        # 存储喜欢第i顶帽子的人
        person_to_hats = [[] for _ in range(41)]
        for p, hat in enumerate(hats):
            for h in hat:
                # print(h)
                person_to_hats[h].append(p)

        # print(person_to_hats)
        f[0][0] = 1
        for i in range(1, maxHatId+1):
            for mask in range(1 << n):
                f[i][mask] = f[i-1][mask]
                for j in person_to_hats[i]:
                    if mask & (1 << j):
                        f[i][mask] += f[i-1][mask ^ (1 << j)]
                f[i][mask] %= mod

        # print(f[:maxHatId+1])
        return f[maxHatId][(1<<n) - 1]


if __name__ == '__main__':
    sol = Solution()
    s = sol.numberWays([[3,4],[4,5],[5]])
    print(s)
    s = sol.numberWays([[3,5,1],[3,5]])
    print(s)
    s = sol.numberWays([[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]])
    print(s)
    s = sol.numberWays([[1,2,3],[2,3,5,6],[1,3,7,9],[1,8,9],[2,5,7]])
    print(s)
    # s = sol.numberWays([[4,15,16,26,28],[1,2,3,4,6,7,8,10,13,14,15,16,17,18,19,21,22,24,25,27,28,29,30],[1,2,3,4,5,7,9,10,11,12,14,15,17,18,19,20,21,22,23,24,25,28,29,30],[2,3,6,7,14,16,17,18,19,20,21,24,25,27,28,29],[1,10],[1,5,6,7,8,9,10,11,13,14,15,16,19,20,21,22,24,25,27,28],[2,5,10,14,16,19,21,22,23,27,30]])
    # print(s)