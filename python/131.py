from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq
import copy

class Solution:
    def partition(self, s: str) -> List[List[str]]:

        @lru_cache(None)
        def isPalindrome(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return  True

        # it can be divied when the divide(s, l, m) and the  divide(s, m, r) are not empty.
        def divide(s, l, r):
            if l == r:
                return []
            elif l + 1 == r:
                return [[s[l]]]
            ret = []
            if isPalindrome(s, l, r-1):
                ret.append([s[l:r]])
            for m in range(l, r):
                if isPalindrome(s, l, m):
                    left = [s[l:m+1]]
                    right = divide(s, m+1, r)
                    for rs in right:
                        ret.append( left + rs )

            return ret

        return divide(s, 0, len(s))


if __name__ == '__main__':
    sol = Solution()
    s = sol.partition('abbba')
    print(s)

