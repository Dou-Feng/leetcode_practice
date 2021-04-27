class Solution:
    def keyboard(self, k: int, n: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * 27 for _ in range(n+1)]
        comb = [[0] * (k+1) for _ in range(n+1)]
        for i in range(n+1):
            comb[i][0] = 1
        for i in range(1, n+1):
            for j in range(1, k+1):
                comb[i][j] = comb[i-1][j] + comb[i-1][j-1]
                # print(i, j, comb[i][j])
        
        for j in range(27):
            dp[0][j] = 1
        for i in range(1, n+1):
            for j in range(1, 27):
                for x in range(min(i, k)+1):
                    dp[i][j] = (dp[i][j] + dp[i-x][j-1] * comb[i][x]) % MOD
                    # print(i, x, comb[i][x])

        return dp[n][26]


sol = Solution()

s = sol.keyboard(2, 4)

print(s)