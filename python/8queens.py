from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def valid(queens, row, column):
            for i, queen in enumerate(queens):
                if queen == column:
                    return False
                u_row_1 = ((row - i) + column) if (row - i) + column < n else -1
                u_row_2 = (column - (row - i)) if column - (row - i) >= 0 else -1
                print("valid", queens, row, column, u_row_1, u_row_2)
                if queen == u_row_1 or queen == u_row_2:
                    return False
            
            return True
        
        queens = []
        ret = []
        def dfs(row):
            if row == n:
                # add to ret
                tmp = [["."] * n for _ in range(n)]
                for i, queen in enumerate(queens):
                    tmp[i][queen] = 'Q'
                layout = []
                for i in range(n):
                    line = ""
                    for c in tmp[i]:
                        line += c
                    layout.append(line)
                ret.append(layout)
                return
            
            for i in range(n):
                if valid(queens, row, i):
                    # print(queens, row, i)
                    queens.append(i)
                    dfs(row+1)
                    queens.pop()
            
        dfs(0)
        return ret

sol = Solution()
print(sol.solveNQueens(4))

