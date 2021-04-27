class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(n):
            if n == 0:
                return 1
            y = pow(n // 2)
            return y * y if n % 2 == 0 else y * y * x

        return pow(n) if n >= 0 else 1 / pow(-n)
                

sol = Solution()
print(sol.myPow(2.00000,-2147483648))
                
        