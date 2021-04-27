from typing import List
import collections
import queue
import bisect
from functools import lru_cache

class Solution:
    def getMaxGridHappiness(self, m: int, n: int, nx: int, wx: int) -> int:

        def cal(x, y):
            if x == 0 or y == 0:
                return 0
            elif x == 2 and y == 2:
                return 40
            elif x == 1 and y == 1:
                return -60
            else:
                return -10

        def print3(x):
            ret = []
            while x:
                ret.append(str(x % 3))
                x //= 3
            if ret:
                print("3bit","".join(ret[::-1]))
            else:
                print("3bit", "0")

        @lru_cache(None)
        def f(loc, mask, nx, wx):
            # print3(mask)
            if nx + wx == 0 or loc == n * m:
                return 0

            x, y = divmod(loc, n)
            mf, mb = mask//(3**(n-1)), mask % 3
            new_mask = mask % (3**(n-1)) * 3
            # print3(mask)
            # print3(new_mask)
            # print(mf, mb)
            # assert(mf == mask//(3**(n-1)))
            ret = f(loc+1, new_mask, nx, wx)

            if nx > 0:
                # print(loc, mask, nx, wx)
                ret = max(ret, f(loc+1, new_mask+1, nx-1, wx ) + 120 + cal(1, mf) + (cal(1, mb) if y>0 else 0))
            if wx > 0:
                ret = max(ret, f(loc+1, new_mask+2, nx, wx-1 ) + 40 + cal(2, mf) + (cal(2, mb) if y>0 else 0))

            return ret

        return f(0, 0, nx, wx)



if __name__ == "__main__":
    sol = Solution()
    s = sol.getMaxGridHappiness(2,3,1,2)
    print(s)
    s = sol.getMaxGridHappiness(3,1,2,1)
    print(s)

