from typing import List

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        n = len(A)
        i, j = 0, n-1
        while i <= j:
            t = A[i]
            if t % 2 == 0:
                i += 1
            else:
                A[i] = A[j]
                A[j] = t
                j -= 1
        
        # blend
        mid = i # A[:i] 全为偶数
        print(A, mid, A[mid])
        for i in range(mid // 2):
            j = 2 * i + 1
            k = (n-1) - ((n-1) % 2) - 2*i
            t = A[k]
            A[k] = A[j]
            A[j]= t

        return A

import random

sol = Solution()
A = []
n = random.randint(1, 100)
odd = True
for i in range(2 * n):
    if odd:
        A.append(random.randint(0, 500) * 2 + 1)
        odd = False
    else:
        A.append(random.randint(0, 500) * 2)
        odd = True

B = sol.sortArrayByParityII(A)
print(B)
for i in range(len(B)):
    if i % 2 == 1 and B[i] % 2 != 1 or i % 2 == 0 and B[i] % 2 != 0:
        print(i, B[i], "Fasle")
