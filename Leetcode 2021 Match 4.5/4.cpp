#include <bits/stdc++.h>

using namespace std;

#define VALID (nx >= 0 && nx < m && ny >= 0 && ny < n)

typedef pair<int, int> PII;
bool vis[105][55][55][2][2][2];
class Solution {
public:
    vector<vector<string>> maze;
    int T, m, n;
    int dx[4] = {1, -1, 0, 0}, dy[4] = {0, 0, 1, -1};
    void dfs(int t, int x, int y, int used1, int used2, int inloc) {
        if (vis[t][x][y][used1][used2][inloc]) return;
        vis[t][x][y][used1][used2][inloc] = true;
        // cout << "mov " << x << ", " << y << endl;
        // 搜索的退出条件
        // 1. 直线距离都无法到达；2. 四周无路可走（陷阱（且没有卷轴可以使用），边界）3. 满足要求
        if (x == m-1 && y == n-1) {
            // cout << t << "; Mov " << x << ", " << y << "; used1 = " << used1 << ", used2 = " << used2 << endl;
            return;
        }

        if ((m-1-x) + (n-1-y) + t >= T) {
            return;
        }
        
        // cout << t << "; Mov " << x << ", " << y << "; used1 = " << used1 << ", used2 = " << used2 << endl;
        // 只有当前位置为 '.' 或者使用了永久卷轴并且没有离开过才可以一直站在这里不动
        if (maze[t+1][x][y] == '.' || inloc)
            dfs(t+1, x, y, used1, used2, inloc);
        
        // 选择移动
        int nx, ny;
        for (int i = 0; i < 4; ++i) {
            nx = x + dx[i], ny = y + dy[i];
            if (VALID) {
                // 如果下一个位置不是陷阱，那么可以直接走过去
                if (maze[t+1][nx][ny] == '.')
                    dfs(t+1, nx, ny, used1, used2, 0);
                else {
                    // 如果是陷阱，考虑使用卷轴
                    if (!used1) dfs(t+1, nx, ny, 1, used2, 0);
                    if (!used2) dfs(t+1, nx, ny, used1, 1, 1);
                }
            }
        }

    }


    bool escapeMaze(vector<vector<string>>& maze) {
        T = maze.size(), m = maze[0].size(), n = maze[0][0].size();
        // cout << T << ", " << m << ", " << n << endl;
        this->maze = maze;
        memset(vis, 0, sizeof(vis));
        dfs(0, 0, 0, 0, 0, 0);
        for (int t = 0; t < T; ++t) {
            for (int u = 0; u < 2; ++u) {
                for (int v = 0; v < 2; ++v) {
                    for (int l = 0; l < 2; ++l) 
                        if (vis[t][m-1][n-1][u][v][l]) return true;
                }
            }
        }
        return false;
    }
};

#define CASE 1

int main() {
    Solution sol;
#if CASE == 1
    vector<vector<string>> input = {{".#.","#.."}, {"...",".#."}, {".##",".#."}, {"..#",".#."}};
#elif CASE == 2
vector<vector<string>> input = {{".#.","..."},{"...","..."}};
#elif CASE == 3
vector<vector<string>> input = {{"...","...","..."},{".##","###","##."},{".##","###","##."},{".##","###","##."},{".##","###","##."},{".##","###","##."},{".##","###","##."}};
#elif CASE == 4
vector<vector<string>> input = {{"..###..##."},{"..######.."},{".#.#..#.#."},{".##..#.##."},{".########."},{".#..##...."},{".#.#####.."},{".###.###.."},{".########."},{".##.##.##."},{".###...##."},{".#####.#.."},{".##..###.."},{"..#####.#."},{".####.###."},{".###.###.."},{"..######.."}};
#endif
    
    cout << sol.escapeMaze(input) << endl;

    return 0;
}