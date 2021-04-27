import bisect
from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = nums
        n = len(a)
        for i in range(n-1, 0, -1):
            if a[i-1] < a[i]:
                j = bisect.bisect_right(a[i:][::-1], a[i-1])
                print(a[i:][::-1], j)
                j = (n-i) - j - 1
                print(i, j)
                tmp = a[i+j]
                a[i+j] = a[i-1]
                a[i-1] = tmp
                # print("A", a)
                b = a[i:]
                b.sort()
                for j in range(n - i):
                    a[i+j] = b[j]
                # print(a)
                return a

        a.sort()
        return a


sol = Solution()
print(sol.nextPermutation([1,5,1]))