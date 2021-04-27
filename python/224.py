from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq
import copy


class Solution:
    def calculate(self, s: str) -> int:
        stack = [1]
        sign, ret, num = 1, 0, 0
        for ch in s:
            if ch.isdigit():
                num = num * 10 + ord(ch) - ord('0')
                continue
            ret += sign * num
            num = 0
            if ch == '-':
                sign = -stack[-1]
            elif ch == '+':
                sign = stack[-1]
            elif ch == '(':
                stack.append(sign)
            elif ch == ')':
                stack.pop()

        ret += sign * num
        return ret

if __name__ == '__main__':
    sol = Solution()
    s = sol.calculate("(7)-(0)+(4)")
    print(s)
    s = sol.calculate(s = "(1+(4+5+2)-3)+(6+8)")
    print(s)
    s = sol.calculate(s = " 2-1 + 2 ")
    print(s)
    s = sol.calculate(s = " 1+1 ")
    print(s)