from typing import List
import copy
class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        print(n, m)
        def elim_island(n_grid, i, j):
            n_grid[i][j] = 0
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for direct in directions:
                nx, ny = i + direct[0], j + direct[1]
                if 0 <= nx < n and 0 <= ny < m and n_grid[nx][ny] == 1:
                    # print(i, j, nx, ny)
                    elim_island(n_grid, nx, ny)

        def qualify(n_grid):
            land_num = 0
            for i in range(n):
                for j in range(m):
                    if n_grid[i][j] == 1:
                        # print(i, j, n_grid)
                        elim_island(n_grid, i, j)
                        # print(n_grid)
                        land_num += 1
            return land_num != 1
        
        if qualify(copy.deepcopy(grid)):
            return 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if (qualify(copy.deepcopy(grid))):
                        return 1
                    grid[i][j] = 1

        return 2


sol = Solution()
# print(sol.minDays([[1, 1]]))
# print(sol.minDays([[0,1,1,0],[0,1,1,0],[0,0,0,0]]))
print(sol.minDays([[1,1,1,1], [1,1,1,1], [1,1,0,1]]))



