from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq
import copy


class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        n = len(nums)
        # graph
        g = [[] for _ in range(n)]
        # stack to store tuple (level, no) containing the node's level and No.
        #  consider the number is range from 1 to 50.
        stk = [[] for _ in range(51)]

        # init the graph
        for e in edges:
            f, t = e[0], e[1]
            g[f].append(t)
            g[t].append(f)

        def gcd(a, b):
            return gcd(b, a % b) if a % b else b

        ans = [-1] * n
        def dfs(cur, pre, depth):
            nonlocal ans
            # get the deepest elem from stack
            maxd, no = -1, -1
            for i in range(51):
                # the level is deeper and the gcd between them is fit.
                # if stk[i]:
                    # print(nums[stk[i][-1][1]], nums[cur], "gcd", gcd(nums[stk[i][-1][1]], nums[cur]), "maxd", maxd, "stk")
                if stk[i] and gcd(nums[stk[i][-1][1]], nums[cur]) == 1 and maxd < stk[i][-1][0]:
                    # print("maxd:", stk[i][-1][0], ", no:", no)
                    maxd = stk[i][-1][0]
                    no = stk[i][-1][1]

            ans[cur] =  no

            # search nodes in the next level
            for node in g[cur]:
                if node == pre:
                    continue
                stk[nums[cur]].append((depth, cur))
                # print("cur", cur, ", node", node)
                dfs(node, cur, depth+1)
                stk[nums[cur]].pop()

        # stk[nums[0]].append((0, 0))
        dfs(0, -1, 0)
        return ans



if __name__ == '__main__':
    sol = Solution()
    s = sol.getCoprimes(nums = [5,6,10,2,3,6,15], edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]])
    print(s)