class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)
        f = [[10**9+7] * (n+1) for _ in range(n+1)]
        f[0][0] = 0

        def cost(num):
            if num == 1:
                return 1
            elif num < 10:
                return 2
            elif num < 100:
                return 3
            else:
                return 4

        for i in range(1, n+1):
            for j in range(0, k+1):
                # 直接删除第i个字符
                if j > 0:
                    f[i][j] = min(f[i][j], f[i-1][j-1])

                # 考虑不删除第i个字符
                # 统计连续的与s[i]相等的字符个数
                same, diff = 0, 0
                for i0 in range(i, 0, -1):
                    if diff > j:
                        break
                    if s[i0-1] == s[i-1]:
                        same += 1
                        f[i][j] = min(f[i][j], f[i0-1][j - diff] + cost(same))
                    else:
                        diff += 1
        return f[n][k]



