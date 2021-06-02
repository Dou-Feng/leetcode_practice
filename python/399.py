from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        cache = {}

        def dfs(div, dividend):
            if div == dividend:
                return 1.0
            formula = div + "/" + dividend
            if formula in cache:
                return cache

            ## find l1 and l2
            l1 = []
            l2 = []
            for i, equ in enumerate(equations):
                d, dv = equ[0], equ[1]
                if d == div or dv == div:
                    l1.append(i)
                elif dv == dividend or d == dividend:
                    l2.append(i)
            
            ## dfs to get the answer
            ans = -1.0
            for i in l1:
                for j in l2:
                    d1, dv1 = (equations[i][0], equations[i][1]) if equations[i][0] == div else (equations[i][1], equations[i][0])
                    v1 = values[i] if equations[i][0] == div else 1.0 / values[i]
                    d2, dv2 = (equations[j][0], equations[j][1]) if equations[j][1] == dividend else (equations[j][1], equations[j][0])
                    v2 = values[j] if equations[j][1] == dividend else 1.0 / values[j]
                    res = v1 * dfs(d2, dv1) * v2
                    if res < 0 or (ans > 0 and res != ans):
                        cache[formula] = -1.0
                        return -1.0
            cache[formula] = ans
            return ans

        ret = []
        for q in queries:
            ret.append(dfs(q[0], q[1]))
        return ret



if __name__ == '__main__':
    sol = Solution()
    s = sol.calcEquation(equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]])
    print(s)