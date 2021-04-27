lass Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.
        elif n == -1:
            return float(1 / x) if x else inf
        elif n == 1:
            return x
        else:
            res = self.myPow(x, abs(n)//2)**2 * (x if n % 2 != 0 else 1)
            if n > 0:
                return res
            else:
                return 1 / res if res else math.inf

sol = Solution()
for i in range(1, -2000000000):
    print(i, sol.cuttingRope(i))