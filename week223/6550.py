from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect

## 不带权值的并查集
class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.weight = [0] * n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y, value):
        rootx = self.find(x)
        rooty = self.find(y)

        if rootx == rooty:
            return False

        self.parent[rootx] = rooty
        return True

    def isConnected(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        if rootx == rooty:
            return True
        return False

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        uf = UF(n)
        for e in allowedSwaps:
            uf.union(e[0], e[1], 0)
            # uf.union(e[1], e[0], 0)

        groups = collections.defaultdict(list)
        for i in range(n):
            groups[uf.find(i)].append(i)
        # print(groups.values())
        same = 0
        for g in groups.values():
            sr, tr = collections.defaultdict(int), collections.defaultdict(int)
            for index in g:
                sr[source[index]] += 1
                tr[target[index]] += 1

            for k, e in sr.items():
                same += min(e, tr[k])

        return n - same



if __name__ == '__main__':
    sol = Solution()
    s = sol.minimumHammingDistance([41,37,51,100,25,33,90,49,65,87,11,18,15,18],
[41,92,69,75,29,13,53,21,17,81,33,19,33,32],
[[0,11],[5,9],[6,9],[5,7],[8,13],[4,8],[12,7],[8,2],[13,5],[0,7],[6,4],[8,9],[4,12],[6,1],[10,0],[10,2],[7,3],[11,10],[5,2],[11,1],[3,0],[8,5],[12,6],[2,1],[11,2],[4,9],[2,9],[10,6],[12,10],[4,13],[13,2],[11,9],[3,6],[0,4],[1,10],[5,11],[12,1],[10,4],[6,2],[10,7],[3,13],[4,5],[13,10],[4,7],[0,12],[9,10],[9,3],[0,5],[1,9],[5,10],[8,0],[12,11],[11,4],[7,9],[7,2],[13,9],[12,3],[8,6],[7,6],[8,12],[4,3],[7,13],[0,13],[2,0],[3,8],[8,1],[13,6],[1,4],[0,9],[2,3],[8,7],[4,2],[9,12]])
    print(s)
    s = sol.minimumHammingDistance([39,8,30,78,66,96,39,9,8,63,100,4,4,16,43,76,25,84,91,52,12,48],
[79,25,30,2,76,83,42,26,87,82,97,81,45,95,16,76,8,26,59,52,21,28],
[[6,9],[7,12],[1,17],[7,0],[18,19],[10,0],[7,3],[11,1],[7,6],[4,19],[21,9],[17,20],[14,18],[5,18],[0,4],[20,13],[18,20],[8,15],[4,10],[6,2],[11,5],[4,16],[14,15],[21,5],[11,21],[19,16],[18,17],[2,17],[14,16],[0,1],[1,12],[12,8],[15,4],[11,2],[3,18],[14,10],[8,18],[21,14],[6,1],[19,9],[16,15],[16,11],[1,21],[7,21],[14,0],[3,11],[1,15],[2,12],[3,17],[6,14],[21,0],[15,7],[20,21],[1,5],[6,3],[20,9],[14,19],[17,5],[7,18],[19,1],[21,18],[8,0],[4,11],[2,7],[6,4],[8,7],[5,7],[5,20],[20,11],[7,17],[3,1],[8,13],[4,8],[15,10],[19,8],[14,11],[11,7],[17,6],[19,11],[20,7],[20,12],[2,19],[10,3],[13,4],[8,16],[6,15],[19,21],[14,7],[12,14],[13,7],[2,20],[3,9],[2,14],[8,6],[19,0],[15,21],[12,19],[18,1],[21,17],[13,18],[1,7],[4,3],[4,2],[9,12],[7,4],[5,6],[19,5],[10,21],[16,0],[7,16],[14,3],[2,1],[4,9],[9,15],[12,5],[3,20],[12,10],[17,9],[11,18],[19,17],[13,3],[8,11],[16,20],[4,14],[2,10],[5,15],[3,19],[17,8],[14,20],[4,20],[19,20],[6,19],[15,12],[17,11],[2,21],[8,3],[12,13]])
    print(s)
    s = sol.minimumHammingDistance(source = [5,1,2,4,3], target = [1,5,4,2,3], allowedSwaps = [[0,4],[4,2],[1,3],[1,4]])
    print(s)
    s = sol.minimumHammingDistance(source = [1,2,3,4], target = [2,1,4,5], allowedSwaps = [[0,1],[2,3]])
    print(s)