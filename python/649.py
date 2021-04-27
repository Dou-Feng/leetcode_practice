from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # get the Radiants and Dires
        n = len(senate)
        rad, dires = queue.deque(), queue.deque()
        for i in range(n):
            if senate[i] == 'R':
                rad.append(i)
            else:
                dires.append(i)

        i = n
        while rad and dires:
            if rad[0] < dires[0]:
                rad.append(i)
            else:
                dires.append(i)
            
            rad.popleft()
            dires.popleft()
            i += 1

        return "Radiant" if rad else "Dire"

        

if __name__ == '__main__':
    sol = Solution()
    s = sol.predictPartyVictory("RD")
    print(s)
    s = sol.predictPartyVictory("RDD")
    print(s)