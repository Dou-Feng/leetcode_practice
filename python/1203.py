from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq

class Solution:
    def topSort(self, items, indegree, pokes):
        que = queue.deque()
        for item in items:
            if not indegree[item]:
                que.append(item)
        # print(que)
        if not que:
            return []

        res = []
        while que:
            top = que.popleft()
            res.append(top)

            for launch in pokes[top]:
                indegree[launch] -= 1
                if indegree[launch] == 0:
                    que.append(launch)

        return res

    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        max_grp = m
        for i in range(n):
            if group[i] == -1:
                group[i] = max_grp
                max_grp += 1
        # print(group)
        indegree = [0] * n
        grp_indegree = [0] * max_grp
        edge = [[] for _ in range(n)]
        grp_edge = [[] for _ in range(max_grp)]
        task_to_grp = [[] for _ in range(max_grp)]
        for i, items in enumerate(beforeItems):
            task_to_grp[group[i]].append(i)
            for pre in items:
                # if they're in the same group
                if group[i] == group[pre]:
                    indegree[i] += 1
                    edge[pre].append(i)
                else:
                    grp_indegree[group[i]] += 1
                    grp_edge[group[pre]].append(group[i])

        # print(max_grp, grp_indegree, grp_edge)
        groupRank = self.topSort([i for i in range(max_grp)], grp_indegree, grp_edge)
        # print(groupRank)
        # if the sorted group is smaller than max_grp
        if len(groupRank) != max_grp:
            return []

        ret = []
        for g in groupRank:
            gelem = self.topSort(task_to_grp[g], indegree, edge)
            if len(gelem) != len(task_to_grp[g]):
                return []
            ret += gelem

        return ret




if __name__ == '__main__':
    sol = Solution()
    # s = sol.sortItems(n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]])
    # print(s)
    s = sol.sortItems(3, 1,
[-1,0,-1],
[[],[0],[1]])
    print(s)