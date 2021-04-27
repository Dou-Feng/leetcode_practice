from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq
import copy

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # 得到一颗最小生成树
        new_edges = [(e[0], e[1], e[2], i) for i, e in enumerate(edges)]
        new_edges.sort(key = lambda e : e[2])
        # print(new_edges)
        uf = UF(n)
        mst_edges = []
        for edge in new_edges:
            f, t, v = edge[0], edge[1], edge[2]
            if uf.union(f, t, v):
                mst_edges.append(edge[3])
            if uf.num == n-1:
                break
        # 最小的权值
        min_weight = uf.v
        # print("Min weight", min_weight)
        msts = []
        def dfs(i, res, ufd):
            nonlocal msts
            # 如果ufd已经形成了最小生成树
            # print(ufd.v, ufd.num, min_weight, n-1)
            if ufd.v <= min_weight and ufd.num == n-1:
                # print("Add to msts")
                msts.append(res.copy())
                return
            if ufd.v > min_weight or i >= len(edges):
                return
            # 选择这条边
            new_ufd = UF(n)
            new_ufd.parent = ufd.parent.copy()
            new_ufd.num = ufd.num
            new_ufd.v = ufd.v
            # print(new_ufd.parent, ufd.parent)
            if new_ufd.union(new_edges[i][0], new_edges[i][1], new_edges[i][2]):
                # print("add edge", i, "new_ufd.weight", new_ufd.v, "new_ufd.num", new_ufd.num)
                res.append(new_edges[i][3])
                dfs(i+1, res, new_ufd)
                res.pop()
            # 不选择这条边
            dfs(i+1, res, ufd)


        dfs(0, [], UF(n))
        # print("msts", msts)
        # 在msts中找到共同的元素
        dic = collections.defaultdict(int)
        for mst in msts:
            for index in mst:
                dic[index] += 1

        key_edge, non_key_edge = [], []
        for key, e in dic.items():
            if e == len(msts):
                key_edge.append(key)
            else:
                non_key_edge.append(key)

        return [key_edge, non_key_edge]


## 不带权值的并查集
class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.num = 0
        self.v = 0

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
        self.num += 1
        self.v += value
        return True


if __name__ == '__main__':
    sol = Solution()
    # s = sol.findCriticalAndPseudoCriticalEdges(n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]])
    # print(s)
    s = sol.findCriticalAndPseudoCriticalEdges(n = 4, edges = [[0,3,1],[0,1,1],[1,2,1],[2,3,1]])
    print(s)