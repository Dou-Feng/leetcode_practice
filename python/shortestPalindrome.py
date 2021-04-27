class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        for l in range(1, n):
            for i in range(n - l):
                j = i + l
                if s[i] == s[j]:
                    if i+1 == j:
                        dp[i][j] = True
                    elif dp[i+1][j-1] == True:
                        dp[i][j] = True
                        print(i, j, "True")
        max_l = 0
        for i in range(n):
            if dp[0][i]:
                max_l = i

        append = s[max_l+1:]
        print(append)
        return append[::-1] + s


sol = Solution()
print("Solution:", sol.shortestPalindrome("aacecaaa"))