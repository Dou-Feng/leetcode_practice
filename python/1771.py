from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq
import copy

class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        word = word1 + word2
        l = m + n
        dp = [[0] * (l+2) for _ in range(l+2)]
        for i in range(l):
            dp[i][i+1] = 1
        ret = 0
        for i in range(l-1, -1, -1):
            for j in range(i+1, l):
                if word[i] == word[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                    if i < m and j >= m:
                        ret = max(ret, dp[i][j])
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])

        return ret

if __name__ == '__main__':
    sol = Solution()
    s = sol.longestPalindrome(word1 = "ab", word2 = "ab")
    print(s)
    s = sol.longestPalindrome(word1 = "cacb", word2 = "cbba")
    print(s)
    s = sol.longestPalindrome(word1 = "aa", word2 = "bb")
    print(s)
    s = sol.longestPalindrome("ceebeddc", "d")
    print(s)