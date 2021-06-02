#include <bits/stdc++.h>

using namespace std;

#define VALID (nx >= 0 && nx < m && ny >= 0 && nx < n)

typedef pair<int, int> PII;


// 用dp(t, i, j, u, v) 表示时间为 t，位置为（i，j），使用了 u 张临时卷轴，v 张永久卷轴的可达性
// 答案为 dp(t, m-1, n-1, u, v)，只要其中一个为 true 答案就为 true
bool dp[101][51][51][2][2];
bool vis[51][51][2];
// dp 解法
class Solution {
public:
    bool escapeMaze(vector<vector<string>>& maze) {
        int T = maze.size(), m = maze[0].size(), n = maze[0][0].size();
        dp[0][0][0][0][0] = true;
        for (int t = 1; t < T; ++t)
        for (int i = 0; i < m; ++i)
        for (int j = 0; j < n; ++j)
        for (int u = 0; u < 2; ++u)
        for (int v = 0; v < 2; ++v) {
            if (dp[t-1][i][j][u][v] ||
                i > 0 && dp[t-1][i-1][j][u][v] ||
                j > 0 && dp[t-1][i][j-1][u][v] || 
                i < m - 1 && dp[t-1][i+1][j][u][v] ||
                j < n - 1 && dp[t-1][i][j+1][u][v]) {
                    if (maze[t][i][j] == '.') {
                        dp[t][i][j][u][v] = 1;
                    } else {
                        if (!u) {
                            dp[t][i][j][1][v] = true;
                        }
                        if (!v) {
                            if (!vis[i][j][u]) {
                                for (int k = t; k < T; ++k) dp[k][i][j][u][1] = true;
                            }
                            vis[i][j][u] = true;
                        }
                    }
                }
        }

        for (int t = 0; t < T; ++t)
        for (int u = 0; u < 2; ++u)
        for (int v = 0; v < 2; ++v)
        if (dp[t][m-1][n-1][u][v]) return true;
        
        return false;
    }
};

#define CASE 2

int main() {
    Solution sol;
#if CASE == 1
    vector<vector<string>> input = {{".#.","#.."}, {"...",".#."}, {".##",".#."}, {"..#",".#."}};
#elif CASE == 2
vector<vector<string>> input = {{".#.","..."},{"...","..."}};
#elif CASE == 3
vector<vector<string>> input = {{"...","...","..."},{".##","###","##."},{".##","###","##."},{".##","###","##."},{".##","###","##."},{".##","###","##."},{".##","###","##."}};
#elif CASE == 4
vector<vector<string>> input = {{".################.",".################.",".################."},{".################.",".################.",".################."},{".################.",".################.",".################."},{".################.",".################.",".################."},{".################.",".################.",".################."},{".################.",".################.",".################."}};
#endif
    
    cout << sol.escapeMaze(input) << endl;

    return 0;
}