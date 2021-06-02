from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq
import copy

class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        i = 0
        seg = queue.deque()
        ret = 0
        n = len(A)
        while i < n:
            if seg and seg[0] <= i:
                seg.popleft()
            l = len(seg)
            # print("i", i, "l", l, seg)
            if (l % 2 == 0 and A[i] == 0) or (l % 2 == 1 and A[i]):
                # print("Reverse, i =", i, ", l =", l)
                if i + K > n:
                    return -1
                seg.append(i + K)
                ret += 1
            i += 1

        return ret



if __name__ == '__main__':
    sol = Solution()
    s = sol.minKBitFlips(A = [0,1,0], K = 1)
    print(s)
    s = sol.minKBitFlips(A = [1,1,0], K = 2)
    print(s)
    s = sol.minKBitFlips([0,0,0,1,0,1,1,0], K = 3)
    print(s)
    s = sol.minKBitFlips([0,1,0,1,0], K = 2)
    print(s)