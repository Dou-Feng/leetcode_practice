from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq
import copy

class Solution:
    def beautySum(self, s: str) -> int:

        def getMinMax(alpha):
            min, max = 10**9+7, -1
            for i in range(26):
                if alpha[i] == 0:
                    continue
                if alpha[i] > max:
                    max = alpha[i]
                if alpha[i] < min:
                    min = alpha[i]

            return min, max

        ret, n = 0, len(s)
        
        for i in range(n):
            alpha = [0] * 26
            alpha[ord(s[i]) - ord('a')] += 1
            for j in range(i+1, n):
                alpha[ord(s[j]) - ord('a')] += 1
                # print(alpha)
                min, max = getMinMax(alpha)
                # print(i, j, min, max)
                ret  += max - min


        return ret




if __name__ == '__main__':
    sol = Solution()
    s = sol.beautySum(s = "aabcbaa")
    print(s)