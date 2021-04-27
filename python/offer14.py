class Solution:
    def cuttingRope(self, n: int) -> int:
        m = n
        dp = [[1] * (m+1) for _ in range(n+1)]

        for i in range(2, n+1):
            for j in range(1, m+1):
                for k in range(1, i-j+2):
                    dp[i][j] = max(dp[i][j], dp[i-k][j-1] * k)
        print(dp[1:][1:])
        return max(dp[n][2:])

sol = Solution()
print(sol.cuttingRope(3))

