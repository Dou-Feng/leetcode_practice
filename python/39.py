from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = 9
        def valid(board, x, y, v):
            for i in range(n):
                if board[x][i] == v or board[i][y] == v:
                    # if x == 0 and y == 5 and v == '8':
                        # print("False at row and col")
                    return False
            seg_x, seg_y = x // 3, y // 3
            for i in range(seg_x*3, seg_x*3+3):
                for j in range(seg_y*3, seg_y*3+3):
                    if board[i][j] == v:
                        # if x == 0 and y == 5 and v == '8':
                            # print(seg_x, seg_y)
                            # print("False small board", i, j)
                        return False
            # if x == 0 and y == 5 and v == '8':
                # print("Success")
            return True

        space = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == '.':
                    space.append((i, j))
        m = len(space)
        # print(space)
        solved = False
        def dfs(i):
            nonlocal solved
            if solved:
                return True
            if i == m:
                # print("solved")
                solved = True
                return True
            for j in range(1, 10):
                x, y = space[i][0], space[i][1]
                # print(x, y, str(j))
                if valid(board, x, y, str(j)):
                    
                    board[x][y] = str(j)
                    dfs(i+1)
                    if solved:
                        return True
                    board[x][y] = '.'

        dfs(0)
        return board

sol = Solution()
s = sol.solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])
print(s)    
