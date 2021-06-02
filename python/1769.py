from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq
import copy

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ret = [0] * n
        for i in range(n):
            op = 0
            for j in range(n):
                if i != j:
                    if boxes[j] == '1':
                        op += abs(j - i)
            ret[i] = op

        return ret

if __name__ == '__main__':
    sol = Solution()
    s = sol.minOperations(boxes = "110")
    print(s)
    s = sol.minOperations(boxes = "001011")
    print(s)