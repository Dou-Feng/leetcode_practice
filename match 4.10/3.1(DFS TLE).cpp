#include <bits/stdc++.h>

using namespace std;

// 正确实现DFS，但是搜索空间太大，导致 TLE

#define INF 0x3f3f3f3f
#define MAX 205

int N;
int edge[MAX][MAX];
bool vis[MAX][MAX];
// dist[i][j] 表示 处于 i 点，还剩 j 电量时，到达 起始点最小代价，结果为 dist[end][0];
int dist[MAX][MAX];
int st, en, tot;
class Solution {
public:
    // 从起点开始搜索，直到搜索到终点
    void dfs(vector<int>& charge, int cur, int power, int cost) {
        // 枝剪
        if (dist[cur][power] <= cost) {
            return;
        } else {
            dist[cur][power] = cost;
            // cout << "(cur, power, dist) = " << cur << ", " << power << ", " << dist[cur][power] << endl;
        }
        // 搜索到终点直接退出
        if (cur == en) return;
        // 选择增加电量
        if (power < tot && !vis[cur][power+1]) {
            vis[cur][power+1] = true;
            dfs(charge, cur, power+1, cost + charge[cur]);
            vis[cur][power+1] = false;
        }

        // 选择往前走
        for (int i = 0; i < N; ++i) {
            if (edge[cur][i] <= power && !vis[i][power-edge[cur][i]]) {
                vis[i][power-edge[cur][i]] = true;
                dfs(charge, i, power-edge[cur][i], cost + edge[cur][i]);
                vis[i][power-edge[cur][i]] = false;
            }
        }
    }
    

    int electricCarPlan(vector<vector<int>>& paths, int cnt, int start, int end, vector<int>& charge) {
        N = charge.size();
        st = start, en = end, tot = cnt;
        memset(vis, 0, sizeof(vis));
        for (int i = 0; i < MAX; ++i)
        for (int j = 0; j < MAX; ++j) {
            edge[i][j] = INF;
            dist[i][j] = INF;
        }

        // 去重边
        for (auto &e : paths) {
            int u = e[0], v = e[1], w = e[2];
            edge[u][v] = min(edge[u][v], w);
            edge[v][u] = min(edge[v][u], w);
        }
        vis[start][0] = true;
        dfs(charge, start, 0, 0);
        return dist[end][0];
    }
};

#define CASE 3

int main() {
    Solution sol;
#if CASE == 1
    vector<vector<int>> path({{1,3,3},{3,2,1},{2,1,3},{0,1,4},{3,0,5}});
    vector<int> charge({2,10,4,1});
    cout << sol.electricCarPlan(path, 6, 1, 0, charge) << endl;
#elif CASE == 2
    vector<vector<int>> path({{0,4,2},{4,3,5},{3,0,5}, {0,1,5},{3,2,4},{1,2,8}});
    vector<int> charge({4,1,1,3,2});

    cout << sol.electricCarPlan(path, 8, 0, 2, charge) << endl;
#elif CASE == 3
    vector<vector<int>> path({{3,7,32},{0,6,46},{1,0,47},{0,6,8},{0,3,30},{1,5,34},{1,2,9},{1,4,29},{0,1,6}});
    vector<int> charge({90,57,24,52,75,61,39,20});

    cout << sol.electricCarPlan(path, 52, 4, 5, charge) << endl;
#elif CASE == 4
    vector<vector<int>> path({{3,2,4},{5,7,1},{6,0,6},{1,7,3},{0,1,6},{3,6,4},{1,7,4},{1,2,1},{3,4,6},{0,3,3},{2,5,1},{0,5,4},{1,0,4},{4,7,1},{6,3,5}});
    vector<int> charge({14,26,95,49,42,90,90,88});

    cout << sol.electricCarPlan(path, 6, 5, 0, charge) << endl;
#endif
    return 0;
}