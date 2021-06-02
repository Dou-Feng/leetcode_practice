from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ret = [first]
        for e in encoded:
            ret.append(ret[-1] ^ e)
        return ret



if __name__ == '__main__':
    sol = Solution()
    s = sol.decode(encoded = [6,2,7,3], first = 4)
    print(s)