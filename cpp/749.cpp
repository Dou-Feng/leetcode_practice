#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <algorithm>

#define debug

using namespace std;

int dx[4] = {0, 1, 0, -1}, dy[4] = {1, 0, -1, 0};

typedef pair<int, int> PII;

class Solution {
private:
    vector<vector<int>> grid; // 访问过的地方变为 - 1
    int m, n;
    set<PII> influence;
    vector<vector<bool>> visited;
    vector<PII> cord;
public:
    inline bool isValid(int x, int y) const {
        return x >= 0 && x < m && y >= 0 && y < n;
    }

    // int bfs(int x, int y) {
    //     queue<pair<int, int>> que;
    //     que.push(make_pair(x, y));
    //     visited[x][y] = true;
    //     int nx, ny, ret = 0;
    //     while (!que.empty()) {
    //         x = que.front().first, y = que.front().second;
    //         cord.emplace_back(que.front());
    //         que.pop();
    //         for (int i = 0; i < 4; ++i) {
    //             nx = x + dx[i], ny = y + dy[i];
    //             if (isValid(nx, ny) && !visited[nx][ny]) {
    //                 // 考虑如果是 1，那么需要加入队列
    //                 if (grid[nx][ny] == 1) {
    //                     visited[nx][ny] = true; 
    //                     que.push(make_pair(nx, ny));
    //                 } else if (grid[nx][ny] == 0) {
    //                     influence.insert({nx, ny});
    //                     ret++;
    //                 }
    //             }
    //         }

    //     }
    //     return ret;
    // }
    
    int dfs(int x, int y) {
        visited[x][y] = true;
        cord.push_back({x, y});
        int nx, ny, ret = 0;
        for (int i = 0; i < 4; ++i) {
            nx = x + dx[i], ny = y + dy[i];
            if (isValid(nx, ny)) {
                if (!grid[nx][ny]) {
                    influence.insert({nx, ny});
                    ret++;
                } else if (grid[nx][ny] == 1 && !visited[nx][ny]) {
                    ret += dfs(nx, ny);
                }
            }
        }
        return ret;
    }
    
    int find() {
        visited = vector<vector<bool>>(m, vector<bool>(n, false));
        int max_area = 0, wall;
        int ret = 0;
        vector<set<PII>> ss;
        vector<PII> path;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n ; ++j) {
                if (!visited[i][j] && grid[i][j] == 1) {
                    cord.clear(), influence.clear();
                    wall = dfs(i, j);

                    if (influence.size() > max_area) {
                        max_area = influence.size();
                        ret = wall;
                        path = cord;
                    }
                    ss.emplace_back(influence);
                }
            }
        }

        for (auto &e : path) grid[e.first][e.second] = -1;
        for (auto &s : ss) {
            if (s.size() != max_area) {
                for (auto &e : s) {
                    grid[e.first][e.second] = 1;
                }
            }
        }
        
        return ret;
    }

    int containVirus(vector<vector<int>>& g) {
        grid = g;
        m = grid.size(), n = grid[0].size();
        int ret = 0, cnt;
        for (;;) {
            cnt = find();
            if (!cnt) break;
            ret += cnt;
        }

        return ret;
    }
};

#define case 4

int main() {
    Solution sol;
#if case == 1
    vector<vector<int>> input({{0,1,0,0,0,0,0,1},
                               {0,1,0,0,0,0,0,1},
                               {0,0,0,0,0,0,0,1},
                               {0,0,0,0,0,0,0,0}});
#elif case == 2
    vector<vector<int>> input({{1,1,1},
 {1,0,1},
 {1,1,1}});
#elif case == 3
    vector<vector<int>> input({{1,1,1,0,0,0,0,0,0},
 {1,0,1,0,1,1,1,1,1},
 {1,1,1,0,0,0,0,0,0}});
#elif case == 4
    vector<vector<int>> input({{0,1,1,1,1,0,1,1,0,0},{0,0,0,0,0,0,1,1,0,0},
                               {0,0,0,0,0,1,0,0,0,1},{0,0,1,0,0,0,0,1,0,0},
                               {1,0,0,0,0,0,1,0,0,0},{0,0,1,1,0,1,0,0,1,0},
                               {0,0,0,0,0,0,0,0,0,1},{0,0,0,0,0,1,1,0,0,0},
                               {0,0,0,1,0,1,0,0,0,0},{0,0,1,0,0,0,0,0,1,0}});
#elif case == 5
    vector<vector<int>> input({{0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0},{1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0},
                               {0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0},{0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
                               {0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0},{0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0},
                               {0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,0,0},{0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0},
                               {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1},{0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0},
                               {0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
                               {0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1},{0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0},
                               {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},{0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
                               {0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0,0},{0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0},
                               {0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0},{1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0}});
#endif
    int n = sol.containVirus(input);
    cout << n;
    return 0;
}