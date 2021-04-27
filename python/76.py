from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq
import copy

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not len(t) or not len(s):
            return ""
        tl = collections.Counter(t)
        # optimize
        sl = collections.defaultdict(int)
        i, n = 0, len(s)
        while i < n and s[i] not in tl:
            i += 1
        j = n-1
        while j >= 0 and s[j] not in tl:
            j -=1
        s = s[i:j+1]
        tset = set(t)

        i, j, n= 0, 0, len(s)
        ri, rj = 0, n
        while j < n:
            if s[j] not in tl:
                j += 1
                continue
            sl[s[j]] += 1
            
            if sl[s[j]] >= tl[s[j]] and s[j] in tset:
                tset.remove(s[j])

            # increment i as far as possible
            while i < j and ( (s[i] not in tl) or (sl[s[i]] > tl[s[i]]) ):
                if sl[s[i]] > 0:
                    sl[s[i]] -= 1
                i += 1
            # print(i, j ,sl)
            if len(tset) == 0 and j - i < rj - ri:
                rj = j
                ri = i
            j += 1

        return s[ri:rj+1] if len(tset) == 0 else ""



if __name__ == '__main__':
    sol = Solution()
    s = sol.minWindow(s = "ADOBECODEBANC", t = "ABC")
    print(s)
    s = sol.minWindow(s = "bba", t = "ba")
    print(s)
    s = sol.minWindow(s = "", t = "a")
    print(s)