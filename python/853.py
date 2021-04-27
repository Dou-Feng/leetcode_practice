from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq
import copy

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted([[position[i], speed[i]] for i in range(len(position))])
        print(cars)
        fleet = len(cars)
        front = (target - cars[fleet-1][0]) / cars[fleet-1][1]
        for i in range(len(cars)-2, -1, -1):
            back = (target - cars[i][0]) / cars[i][1]
            if back <= front:
                fleet -= 1
                # print("form fleet", i)
            else:
                front = back

        return fleet

if __name__ == '__main__':
    sol = Solution()
    s = sol.carFleet(target = 11, position = [10,8,0,5,3], speed = [2,4,1,1,3])
    print(s)