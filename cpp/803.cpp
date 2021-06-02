#include <bits/stdc++.h>

using namespace std;

#define tran(x, y) (((x) * n) + (y)+1)
#define valid(x, y) ((x)>=0 && (x) < m && (y) >= 0 && (y) < n)


class UD {
public:
    vector<int> f;
    vector<int> num;
    UD(int n) : f(vector<int>(n)), num(vector<int>(n, 1)) {
        for (int i = 0; i < n; ++i) {
            f[i] = i;
        }
    }

    int getf(int x) {
        if (x != f[x]) f[x] = getf(f[x]);
        return f[x];
    }

    void add(int x, int y) {
        int px, py;
        px = getf(x);
        py = getf(y);
        if (px != py) {
            f[px] = py;
            num[py] += num[px]; // py的值发生了变化
            
        }
    }
};

class Solution {
public:
    vector<int> hitBricks(vector<vector<int>>& grid, vector<vector<int>>& hits) {
        // 预处理
        int m = grid.size(), n = grid[0].size();
        vector<vector<int>> new_grid(grid);
        // // 测试是否是深拷贝
        for (auto e : hits) {
            new_grid[e[0]][e[1]] = 0;
        }

        UD udf(m*n + 1);
        // 第一排砖块连接到屋顶
        int root = 0;
        for (int i = 0; i < n; ++i) {
            if (new_grid[0][i]) {
                udf.add(root, tran(0, i));
            }
        }
        // 连接接下来的砖块
        for (int i = 1; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (new_grid[i][j]) {
                    // 连接到左边
                    if (j > 0 && new_grid[i][j-1]) {
                        
                        udf.add(tran(i,j), tran(i, j-1));
                    }
                    // 连接到上边
                    if (new_grid[i-1][j]) {
                        udf.add(tran(i, j), tran(i-1, j));
                    }
                }
            }
        }
        vector<int> ans(hits.size(), 0);
        
        // 反序补上砖块
        int dx[] = {0, 0, -1, 1}, dy[] = {1, -1, 0, 0};
        int nx, ny, x, y, add, orign;
        for (int i = hits.size()-1; i>=0; --i) {
            x = hits[i][0], y = hits[i][1];
            // 得存在砖块才补
            if (grid[x][y]) {
                orign = udf.num[udf.getf(root)];
                // 如果是第一排要特殊的连接到屋顶
                if (x == 0) {
                    udf.add(root, tran(x, y));
                }
                // 上下左右都得连接上
                for (int j = 0; j < 4; ++j) {
                    nx = x + dx[j], ny = y + dy[j];
                    
                    if (valid(nx, ny) && new_grid[nx][ny]) {
                        udf.add(tran(x, y), tran(nx, ny));
                    }
                }
                // 补上
                new_grid[x][y] = 1;
                // 计算差值
                add = udf.num[udf.getf(root)];
                if (add - orign) {
                    // 补上的砖不能算
                    ans[i] = add - orign - 1;
                }
            }
        }

        return ans;
    }
};


int main() {
    Solution sol;
    vector<vector<int>> grid({{1,0,0,0}, {1,1,1,0}});
    vector<vector<int>> input({{1,0},{0, 0}});
    vector<int> s = sol.hitBricks(grid, input);
    for (auto v : s) {
        cout << v << endl;
    }
    return 0;
}