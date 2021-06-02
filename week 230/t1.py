from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq
import copy


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        index = 0
        if ruleKey == 'color':
            index = 1
        elif ruleKey == 'name':
            index = 2

        ret = 0
        for e in items:
            if e[index] == ruleValue:
                ret += 1

        return ret


if __name__ == '__main__':
    sol = Solution()
    s = sol.countMatches(items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], ruleKey = "type", ruleValue = "phone")
    print(s)