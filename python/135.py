from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect

class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        def enlarge(base, st, is_left):
            left, right = 0, len(base) - 1
            inc = 1 if is_left else -1
            if not is_left:
                t = left
                left = right
                right = t
            print(base)
            for i in range(left+inc, right+inc, inc):
                if ratings[st+i] > ratings[st+i-inc] and base[i] <= base[i-inc]:
                    base[i] = base[i-inc] + 1
            print(base)

        def sub(left, right):
            if left == right:
                return [1]
            mid = (left + right) // 2
            left_nums = sub(left, mid)
            right_nums = sub(mid+1, right)
            if ratings[mid] > ratings[mid+1] and left_nums[-1] <= right_nums[0]:
                left_nums[-1] = right_nums[0]+1
                enlarge(left_nums, left, False)
            elif ratings[mid] < ratings[mid+1] and left_nums[-1] >= right_nums[0]:
                right_nums[0] = left_nums[-1]+1
                enlarge(right_nums, mid+1, True)
            
            # print("At the range(", left, ",", right, "), the mid is ", mid)
            return left_nums + right_nums
        
        return sum(sub(0, len(ratings)-1)) if ratings else 0


if __name__ == '__main__':
    sol = Solution()
    s = sol.candy([1,2,3,4,0,1,2,0,5,6,7])
    print(s)
    # s = sol.candy([1,2,2])
    # print(s)