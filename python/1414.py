class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib = [1, 1]
        while fib[-1] < k:
            fib.append(fib[-1] + fib[-2])

        # print(len(fib), fib[-1])
        n = len(fib)
        t = 0
        i = n-1
        while k and i:
            if fib[i] == k:
                return t+1
            elif fib[i] < k:
                k -= fib[i]
                t += 1

            i -= 1

        return t


sol = Solution()
print(sol.findMinFibonacciNumbers(19))