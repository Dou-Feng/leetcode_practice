from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq
import copy


class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        left, right = 1, m*n
        def theKcnt(mid):
            cnt = 0
            row, col = 0, n-1
            while row < m and col >= 0:
                if (row+1) * (col+1) <= mid:
                    cnt += (col+1)
                    row += 1
                else:
                    col -= 1
            return cnt
        while left < right:
            mid = (left + right) // 2
            cnt = theKcnt(mid)
            if cnt >= k:
                right = mid
            else:
                left = mid + 1

        return left


        


if __name__ == '__main__':
    sol = Solution()
    s = sol.findKthNumber(11,13,57)
    print(s)