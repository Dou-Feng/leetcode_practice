from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq
import copy

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        ret = 0
        for l in range(1, 27):
            tot = 0
            less = 0
            alpha = [0] * 26
            i = 0
            for j, e in enumerate(s):
                index = ord(e) - ord('a')
                alpha[index] += 1
                if alpha[index] == 1:
                    less += 1
                    tot += 1
                if alpha[index] == k:
                    less -= 1
                # print(i, j, index, less)
                if less == 0:
                    ret = max(ret, j -  i + 1)

                # if total greater than l
                while tot > l:
                    index = ord(s[i]) - ord('a')
                    alpha[index] -= 1
                    if alpha[index] == k-1:
                        less += 1
                    if alpha[index] == 0:
                        less -= 1
                        tot -= 1
                    i += 1

        return ret


if __name__ == '__main__':
    sol = Solution()
    s = sol.longestSubstring(s = "aaabbaaaaa", k = 3)
    print(s)