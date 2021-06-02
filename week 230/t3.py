from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq
import copy


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        l1, l2 = len(nums1), len(nums2)
        if 6 * l1 - l2 < 0 or 6 * l2 - l1 < 0:
            return -1
        sum1, sum2 = sum(nums1), sum(nums2)
        if sum1 < sum2:
            t = nums1
            nums1 = nums2
            nums2 = t
            t = sum1
            sum1 = sum2
            sum2 = t

        diff = sum1 - sum2
        # print(diff)
        op = 0
        cnt1, cnt2 = collections.Counter(nums1), collections.Counter(nums2)
        valid = True
        while diff:
            # print("diff", diff)
            for i in range(6, 1, -1):
                j = 7 - i
                if cnt1[i] > 0:
                    if diff >= i - 1:
                        cnt1[i] -= 1
                        cnt1[1] += 1
                        diff -= i - 1
                    else:
                        diff = 0

                    op += 1
                    choose = True
                    break
                elif cnt2[j] > 0:
                    if diff >= 6 - j:
                        cnt2[j] -= 1
                        diff -= 6 - j
                    else:
                        diff = 0
                    op += 1
                    break

        return op



if __name__ == '__main__':
    sol = Solution()
    s = sol.minOperations([5,2,1,5,2,2,2,2,4,3,3,5], [1,4,5,5,6,3,1,3,3])
    print(s)
    s = sol.minOperations(nums1 = [1,2,3,4,5,6], nums2 = [1,1,2,2,2,2])
    print(s)
    s = sol.minOperations(nums1 = [1,1,1,1,1,1,1], nums2 = [6])
    print(s)
    s = sol.minOperations(nums1 = [6,6], nums2 = [1])
    print(s)