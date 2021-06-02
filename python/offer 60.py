from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq
import copy


class Solution:
    def dicesProbability(self, n: int) -> List[float]:
        
        @lru_cache(None)
        def match(cnt, p):
            if cnt > p or 6 * cnt < p or cnt == 0 or p == 0:
                return 0

            if cnt == 1:
                return 1

            ret = 0
            for i in range(max(1, p-6*cnt+6), min(p-cnt+1, 6) + 1):
                ret += match(cnt-1, p-i)

            return ret
        ans = []
        tot = 6 ** n
        for i in range(n, 6*n+1):
            ans.append(match(n, i) / tot)

        return ans

if __name__ == '__main__':
    sol = Solution()
    s = sol.dicesProbability(2)
    print(s)