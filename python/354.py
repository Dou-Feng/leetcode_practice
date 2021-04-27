from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq
import copy


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort()
        stk = []
        ret = 0
        for i, e in enumerate(envelopes):
            while stk and (envelopes[stk[-1]][0] == e[0] or envelopes[stk[-1]][1] >= e[1]):
                stk.pop()

            stk.append(i)
            ret = max(ret, len(stk))

        return ret

if __name__ == '__main__':
    sol = Solution()
    s = sol.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]])
    print(s)