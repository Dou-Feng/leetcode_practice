from typing import List
import random

class Solution:
    def add(self, num1, num2):
        n = max(len(num1), len(num2))
        m = min(len(num1), len(num2))
        longer_num = num1 if len(num1) > len(num2) else num2
        shorter_num = num2 if len(num1) > len(num2) else num1

        flag = 0
        res = ""
        for i in range(m):
            j = m - 1 - i
            i = n - 1 - i
            ans = int(longer_num[i]) + int(shorter_num[j]) + flag
            flag = ans // 10
            ans = int(ans % 10)
            res += str(ans)
        
        for i in range(m, n):
            i = n - 1 - i
            ans = int(longer_num[i]) + flag
            flag = ans // 10
            ans = int(ans % 10)
            res += str(ans)
        if flag:
            res += "1"
        
        return res[::-1]
        
    def pow(self, s, n):
        for i in range(n):
            s += "0"
        return s
    def multiply(self, num1: str, num2: str) -> str:
        n = len(num1)
        m = len(num2)
        if n < 4 and m < 4:
            return str(int(num1) * int(num2))

        a = num1[:n//2]
        b = num1[n//2:]
        c = num2[:m//2]
        d = num2[m//2:]

        print(a, b, c, d)
        bd = self.multiply(b, d)
        ad = self.pow(self.multiply(a, d), len(b))
        bc = self.pow(self.multiply(b, c), len(d))
        ac = self.pow(self.multiply(a, c), len(b) + len(d))
        print(bd, ad, bc, ac)

        return self.add(bd, self.add(ad, self.add(bc, ac)))

if __name__ == "__main__":
    sol = Solution()
    for i in range(100):
        a = random.randint(0, 1000000000)
        b = random.randint(0, 100000000)
        if sol.multiply(str(a), str(b)) != str(a * b):
            print("Failed")
            exit()
    print("Pass!")
        

