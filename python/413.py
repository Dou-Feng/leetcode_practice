from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect

class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        pre = 0
        ret = 0
        for i in range(2, len(A)):
            if A[i-1] - A[i-2] == A[i] - A[i-1]:
                pre = pre + 1
                ret += pre
            else:
                pre = 0
        return ret
        
if __name__ == '__main__':
    sol = Solution()
    s = sol.numberOfArithmeticSlices([1, 2, 3, 5,5,6,7])
    print(s)
    s = sol.numberOfArithmeticSlices([12,1,-10])
    print(s)
        