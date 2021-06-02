#include <bits/stdc++.h>

using namespace std;

#define INF 0x3f3f3f3f

int N;
int edge[205][205];
bool vis[205][205];
class Solution {
public:
    int electricCarPlan(vector<vector<int>>& paths, int cnt, int start, int end, vector<int>& charge) {
        N = charge.size();
        memset(vis, 0, sizeof(vis));
        for (int i = 0; i < N; ++i)
        for (int j = 0; j < N; ++j)
            edge[i][j] = INF;

        // 去重边
        for (auto &e : paths) {
            int u = e[0], v = e[1], w = e[2];
            edge[u][v] = min(edge[u][v], w);
            edge[v][u] = min(edge[v][u], w);
        }
        // dijkstra
        vector<vector<int>> dist(N, vector<int>(cnt+1, INF));
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> pq;
        dist[start][0] = 0;
        pq.emplace(0, start, 0);
        while (!pq.empty()) {
            auto [d, u, w] = pq.top();
            // cout << "(d, u, w) = " << d << ", " << u << ", " << w << endl;
            pq.pop();
            if (u == end) {
                return d;
            }
            if (d > dist[u][w] || vis[u][w]) continue;
            vis[u][w] = 1;
            
            // neighbor
            for (int i = 0; i < N; ++i) {
                if (edge[u][i] == 0) {
                    cout << u << ", " << i << endl;
                }
                if (edge[u][i] <= w && d + edge[u][i] < dist[i][w - edge[u][i]]) {
                    dist[i][w - edge[u][i]] = d + edge[u][i] ;
                    pq.emplace(dist[i][w - edge[u][i]], i, w - edge[u][i]);
                }
            }

            // charge
            if (w < cnt&& dist[u][w+1] > d + charge[u]) {
                dist[u][w+1] = d + charge[u];
                pq.emplace(dist[u][w+1], u, w+1);
            }
        }
        return 0;
    }
};

#define CASE 2

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