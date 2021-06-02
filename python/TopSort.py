from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq

class Solution:

    def topSort(self, indegree, pokes):
        que = queue.deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                que.append(i)
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

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        pokes = [[] for _ in range(numCourses)]

        for pre in prerequisites:
            pokes[pre[0]].append(pre[1])
            indegree[pre[1]] += 1
        # print(pokes)
        return len(self.topSort(indegree, pokes)) == numCourses



if __name__ == '__main__':
    sol = Solution()
    s = sol.canFinish(2, [[1,0]] )
    print(s)
    s = sol.canFinish(2, [[1,0],[0,1]])
    print(s)