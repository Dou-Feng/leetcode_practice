from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # 首先统计emails都在哪些accounts中出现
        emails = collections.defaultdict(list)
        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                emails[account[j]].append(i)

        # 用并查集构建图
        n = len(accounts)
        uf = UF(n+1)
        for i in range(n):
            for j in range(1, len(accounts[i])):
                for target in emails[accounts[i][j]]:
                    uf.union(i, target)

        # 分组
        groups = collections.defaultdict(list)
        for i in range(n):
            root = uf.find(i)
            groups[root].append(i)

        # 统计每组的邮箱
        ans = []
        for grp in groups.values():
            gmails = set()
            name = accounts[grp[0]][0]
            for no in grp:
                for i in range(1, len(accounts[no])):
                    gmails.add(accounts[no][i])

            ans.append( [name] + sorted(list(gmails)) )

        return ans





class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
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

    def getSize(self, x):
        return self.size[self.find(x)]

if __name__ == '__main__':
    sol = Solution()
    s = sol.accountsMerge([["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]])
    print(s)
    s = sol.accountsMerge([["John",  "john00@mail.com"]])
    print(s)