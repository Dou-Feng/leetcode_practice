from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq
import copy

class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        d = collections.defaultdict(int)
        for w in words:
            k = 0
            for c in w:
                k |= ( 1 << ( ord(c) - ord('a') ) )
            d[k] += 1

        ret = [0] * len(puzzles)
        for j, puzzle in enumerate(puzzles):
            mask = 0

            for i in range(1, 7):
                mask |= ( 1 << ( ord(puzzle[i]) - ord('a') ) )

            subset = mask
            # print(subset)
            while subset:
                s = subset | ( 1 << ( ord(puzzle[0]) - ord('a') ) )
                if s in d:
                    # print(s)
                    ret[j] += d[s]

                subset = mask & (subset - 1)
                # print(subset)

            # consider only the first letter appears in words
            if ( 1 << ( ord(puzzle[0]) - ord('a') ) ) in d:
                ret[j] += d[( 1 << ( ord(puzzle[0]) - ord('a') ) )]

        return ret


if __name__ == '__main__':
    sol = Solution()
    s = sol.findNumOfValidWords(words = ["aaaa","asas","able","ability","actt","actor","access"], \
        puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"])
    print(s)