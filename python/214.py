from functools import lru_cache

class Solution:



    def shortestPalindrome(self, s: str) -> str:
        n = len(s)

        lps = [0] * (n+1)
        i, j = 1, 0
        while i < n:
            if s[i] == s[j]:
                lps[i] = lps[j] + 1
                j += 1
                i += 1
            else:
                if j == 0:
                    lps[i] = 0
                    i += 1
                else:
                    j = lps[j-1]
        print(lps)

        rs = s[::-1]
        i, j= 0, 0
        while i < n:
            while j < n and i < n and rs[i] == s[j]:
                i += 1
                j += 1
            if i == n or j == n:
                ret = "" if j == n else s[j:]
                return ret[::-1] + s
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j-1]
        ret = "" if n == 0 else s[1:]

        return ret[::-1] + s



    # def shortestPalindrome(self, s: str) -> str:
    #     n = len(s)
    #     dp = [[False] * n for _ in range(n)]
    #     for i in range(n):
    #         dp[i][i] = True

    #     for l in range(1, n):
    #         for i in range(n - l):
    #             j = i + l
    #             if s[i] == s[j]:
    #                 if i+1 == j:
    #                     dp[i][j] = True
    #                 elif dp[i+1][j-1] == True:
    #                     dp[i][j] = True
    #                     print(i, j, "True")
    #     max_l = 0
    #     for i in range(n):
    #         if dp[0][i]:
    #             max_l = i

    #     append = s[max_l+1:]
    #     return append[::-1] + s



sol = Solution()
print("Solution:", sol.shortestPalindrome("ab"))