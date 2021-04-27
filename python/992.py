from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq
import copy

class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        n = len(A)
        def atMostKelement(k):
            left, right = 0, 0
            words = dict()
            ret = 0
            while right < n:
                words[A[right]] = right
                if len(words) == k+1:
                    while words[A[left]] != left:
                        left += 1
                    words.pop(A[left])
                    left += 1
                right += 1
                ret += right - left
                
            return ret

        return atMostKelement(K) - atMostKelement(K-1)


if __name__ == '__main__':
    sol = Solution()
    s = sol.subarraysWithKDistinct(A = [1,2,1,2,3], K = 2)
    print(s)
    s = sol.subarraysWithKDistinct(A = [1,2,1,3,4], K = 3)
    print(s)
    s = sol.subarraysWithKDistinct(A = [1,2,1,3,4], K = 1)
    print(s)
    s = sol.subarraysWithKDistinct([27,27,43,28,11,20,1,4,49,18,37,31,31,7,3,31,50,6,50,46,4,13,31,49,15,52,25,31,35,4,11,50,40,1,49,14,46,16,11,16,39,26,13,4,37,39,46,27,49,39,49,50,37,9,30,45,51,47,18,49,24,24,46,47,18,46,52,47,50,4,39,22,50,40,3,52,24,50,38,30,14,12,1,5,52,44,3,49,45,37,40,35,50,50,23,32,1,2],20)
    print(s)