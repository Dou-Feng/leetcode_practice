from typing import List
import bisect

class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        num = 0
        n1, n2 = len(nums1), len(nums2)
        nums1.sort()
        nums2.sort()

        def getNum(src, target):
            ans = 0
            
            i = 0
            tn = len(target)
            sn = len(src)
            while i < tn:
                secu_n = 0
                if i + secu_n + 1 < tn and target[i + secu_n] == target[i + secu_n + 1]:
                    secu_n += 1

                mul = target[i] * target[i]

                for j in range(sn):
                    if mul % src[j] != 0:
                        continue
                    left = bisect.bisect_left(src[j+1:], mul // src[j])
                    right = bisect.bisect_right(src[j+1:], mul // src[j])

                    ans += (secu_n + 1) * (right - left)

                i += secu_n+1

            return ans


        return getNum(nums1, nums2) + getNum(nums2, nums1)


sol = Solution()
print(sol.numTriplets([7,7,8,3], [1,2,9,7]))
print(sol.numTriplets([1,1,1], [1,1,1]))
print(sol.numTriplets([4,7,9,11,23], [3,5,1024,12,18]))
print(sol.numTriplets([7,4], [5,2,8,9]))

