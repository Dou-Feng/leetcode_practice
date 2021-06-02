from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq
import copy
import sys

class BIT:
    def lowbit(self, x):
        return x & (-x)

    def __init__(self, seq):
        self.n = len(seq)
        self.t = [0] * (n+1)
        for x, e in enumerate(seq):
            x += 1
            self.t[x] += e
            j = x + self.lowbit(x)
            if j <= n:
                self.t[j] += self.t[x]

    def add(self, i, x):
        while i <= self.n:
            self.t[i] += x
            i += self.lowbit(i)

    def find(self, i):
        ret = 0
        while i:
            ret += self.t[i]
            i -= self.lowbit(i)

        return ret

    def query(self, l, r):
        return self.find(r) - self.find(l-1)


if __name__ == '__main__':
    line = sys.stdin.readline()[:-1].split(" ")
    n, q = int(line[0]), int(line[1])
    line = sys.stdin.readline()[:-1].split(" ")
    seq = [int(e) for e in line]
    bit = BIT(seq)

    for _ in range(q):
        line = sys.stdin.readline()[:-1].split(" ")
        op, x, y = int(line[0]), int(line[1]), int(line[2])
        if op == 1:
            bit.add(x, y)
        else:
            print(bit.query(x, y))
