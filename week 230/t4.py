from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq
import copy


class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        line = list()
        ans = [0.0] * len(cars)
        line.append(len(cars)-1)
        ans[-1] = -1.0
        for i in range(len(cars)-2, -1, -1):
            while line:
                top = line[-1]
                # 如果当前车速小于顶部车速
                if cars[i][1] <= cars[top][1]:
                    line.pop()
                # 如果当前车速大于前边车的车速，那么考虑是否能够在前车融合之前追上
                else:
                    # 如果前车不消失，那么肯定能追上
                    if ans[top] < 0:
                        break
                    t = (cars[top][0] - cars[i][0]) / (cars[i][1] - cars[top][1])
                    # 已经融合
                    if t > ans[top]:
                        line.pop()
                    else:
                    # 还没融合
                        break

            # print(line)
            if line:
                pop = cars[line[-1]]
                ans[i] = (pop[0] - cars[i][0]) / (cars[i][1] - pop[1])
            else:
                ans[i] = -1.0
            line.append(i)

        return ans

if __name__ == '__main__':
    sol = Solution()
    s = sol.getCollisionTimes(cars = [[1,2],[2,1],[4,3],[7,2]])
    print(s)
    s = sol.getCollisionTimes(cars = [[3,4],[5,4],[6,3],[9,1]])
    print(s)