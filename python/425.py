from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not len(intervals):
            return 0
        intervals.sort(key=lambda x: x[1])
        last = intervals[0][0]
        ret = 0
        for inter in intervals:
            first, second = inter[0], inter[1]
            if first >= last:
                ret += 1
                last = second
        
        return len(intervals) - ret
        


if __name__ == '__main__':
    sol = Solution()
    s = sol.eraseOverlapIntervals([ [1,2], [2,3], [3,4], [1,3] ])
    print(s)
    s = sol.eraseOverlapIntervals([ [1,2], [1,2], [1,2] ])
    print(s)
    s = sol.eraseOverlapIntervals([ [1,2], [2,3] ])
    print(s)
    s = sol.eraseOverlapIntervals([[0,10],[1,2],[2,3],[3,4]])
    print(s)