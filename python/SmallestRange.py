from typing import List
import numpy as np
import queue
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        if k == 1:
            return [nums[0][0], nums[0][0]]
        indices = [0] * k

        maximum = 0
        minimum = 10**9
        min_index = 0
        # 使用优先级队列进行优化
        que = queue.PriorityQueue()
        for i in range(k):
            que.put((nums[i][indices[i]], i))
            if nums[i][indices[i]] > maximum:
                maximum = nums[i][indices[i]]

        minimum, min_index = que.get()
        ret = 10**9
        ret_st = minimum
        ret_te = maximum
        while not que.empty():
            if ret > maximum - minimum:
                ret = maximum - minimum
                ret_st = minimum
                ret_te = maximum

            if indices[min_index] + 1 < len(nums[min_index]):
                indices[min_index] += 1
                que.put((nums[min_index][indices[min_index]], min_index))
                if nums[min_index][indices[min_index]] > maximum:
                    maximum = nums[min_index][indices[min_index]]
                minimum, min_index = que.get()
            else:
                break


        return [ret_st, ret_te]

sol = Solution()
print(sol.smallestRange([[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]))