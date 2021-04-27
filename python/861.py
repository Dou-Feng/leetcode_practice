from typing import List
import collections
import queue
import bisect


class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        m = len(A)
        n = len(A[0])

        for row in range(m):
            if A[row][0] == 0:
                for j in range(n):
                    A[row][j] = 1 if A[row][j] == 0 else 0
        # print(A)
        for col in range(n):
            freq = 0
            for i in range(m):
                if A[i][col] == 0:
                    freq += 1

            if freq > m // 2:
                for i in range(m):
                    A[i][col] = 1 if A[i][col] == 0 else 0
        # print(A)
        ret = 0
        for i in range(m):
            line = 0
            for j in range(n):
                line += 2**(n-j-1) if A[i][j] else 0
            # print(line)
            ret += line

        return ret




if __name__ == "__main__":
    sol = Solution()
    s = sol.matrixScore([[1,1,0,0], [1,0,0,1], [0,0,1,0], [0,1,0,0]])
    print(s)
    s = sol.matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]])
    print(s)
