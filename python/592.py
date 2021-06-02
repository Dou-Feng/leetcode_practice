from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect

class Solution:
    def fractionAddition(self, expression: str) -> str:
        
        def toInt(s):
            nums = s.split('/')
            return int(nums[0]), int(nums[1])

        def simplify(n1, n2):
            return n1 // math.gcd(n1, n2), n2 // math.gcd(n1, n2)

        def add(s1, s2):
            up1, down1 = toInt(s1)
            up2, down2 = toInt(s2)

            up, down = up1*down2+up2*down1, down1*down2
            if up == 0:
                return '0/1'
            up, down = simplify(up, down)
            return str(up) + '/' + str(down)
        
        f1 = '0/1'
        i = 0
        while i < len(expression):
            # get a num
            j = i
            if expression[j] == '+' or expression[j] == '-':
                j += 1
            while j < len(expression) and expression[j] != '+' and expression[j] != '-':
                j += 1
            num = expression[i:j]
            f1 = add(f1, num)
            i = j
        
        return f1

            
            



if __name__ == '__main__':
    print("hello")
    sol = Solution()
    s = sol.fractionAddition("-1/2+1/2")
    print(s)
    s = sol.fractionAddition("-1/2+1/2+1/3")
    print(s)
    s = sol.fractionAddition("1/3-1/2")
    print(s)
    s = sol.fractionAddition("5/3+1/3")
    print(s)
    s = sol.fractionAddition("0")
    print(s)
