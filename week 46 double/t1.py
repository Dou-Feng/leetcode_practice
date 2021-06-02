from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq
import copy


class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        reti, retj = 0, 0
        n = len(s)

        def valid(le, cap):
            for i in range(26):
                if not ((le[i] and cap[i]) or (not le[i] and not cap[i])):
                    return False

            return True
        for i in range(n):
            le, cap = [False] * 26, [False] * 26
            for j in range(i, n):
                if ord('a') <= ord(s[j]) <= ord('z'):
                    t = ord(s[j]) - ord('a')
                    le[t] = True
                else:
                    t = ord(s[j]) - ord('A')
                    cap[t] = True

                if valid(le, cap) and j - i > retj - reti:
                    retj = j
                    reti = i

        return s[reti: retj+1] if retj != 0 else ""



if __name__ == '__main__':
    sol = Solution()
    s = sol.longestNiceSubstring("aaaAadsadBdDb")
    print(s)