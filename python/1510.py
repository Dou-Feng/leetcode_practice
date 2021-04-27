import math

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(1, int(math.sqrt(n))+1):
            dp[i**2] = True
        for i in range(2, n+1):
            if dp[i]:
                continue
            for j in range(1, int(math.sqrt(i)) + 1):
                if dp[i - j**2] == False:
                    # print(i, j, "True")
                    dp[i] = True
                    break
        
        return dp[n]


sol = Solution()
# print(sol.winnerSquareGame(1000))
print(sol.winnerSquareGame(18))
# print(sol.winnerSquareGame(5))
# print(sol.winnerSquareGame(1))
print(sol.winnerSquareGame(7))
# print(sol.winnerSquareGame(20))