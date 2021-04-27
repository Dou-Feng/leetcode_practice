from typing import List
import bisect

class Solution:
    def breakfastNumber(self, staple: List[int], drinks: List[int], x: int) -> int:
        MOD = 10 ** 9 + 7
        staple.sort()
        res = 0
        for d in drinks:
            if d >= x:
                continue
            i = bisect.bisect_right(staple, x - d)
            res = (res + i) % MOD

        return res


sol = Solution()

print(sol.breakfastNumber([10,20,5], [5,5,2], 15))
print(sol.breakfastNumber([2,1,1], [8,9,5,1], 9))
print(sol.breakfastNumber([1], [1], 7))