from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq
import copy


class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        if len(values) == 3:
            return values[0] * values[1] * values[2]
        
        # if the length of values is greater than 3, it indicates we should find the least valuable edge to split the values
        mis, mjs, mm = [], [], 10**9
        n = len(values)
        for i in range(n):
            for j in range(i+2, n):
                if abs(i - j) <= 1 or abs(i - j - n) <= 1 or abs(i + n - j) <= 1:
                    continue
                
                if values[i] * values[j] < mm:
                    mm = values[i] * values[j]
                    mis, mjs = [i], [j]
                elif values[i] * values[j] == mm:
                    mis.append(i)
                    mjs.append(j)
        ret = 10 ** 9
        for i in range(len(mis)):
            mi = mis[i]
            mj = mjs[i]
            edge1, edge2 = [], []
            for k in range(mi, mj+1):
                edge1.append(values[k])
            
            for k in range(mj, mi+n+1):
                edge2.append(values[k % n])
            
            # print("split", edge1, edge2)
            ret = min(ret, self.minScoreTriangulation(edge1) + self.minScoreTriangulation(edge2))

        return ret



if __name__ == '__main__':
    sol = Solution()
    s = sol.minScoreTriangulation([3,3,6,2,1,4])
    print(s)
    s = sol.minScoreTriangulation([3,7,4,5])
    print(s)
    s = sol.minScoreTriangulation([1,3,1,4,1,5])
    print(s)