 #include <bits/stdc++.h>

using namespace std;

#define INF 0x3f3f3f3f

class Solution {
public:
    vector<vector<int>> g;
    int n;
    vector<int> bfs(int u) {
        vector<int> dist(n+1, INF);
        queue<int> q;
        q.push(u);
        dist[u] = 0;
        while (!q.empty()) {
            int f = q.front(); q.pop();
            for (auto& v : g[f]) {
                if (dist[v] > dist[f] + 1) {
                    dist[v] = dist[f] + 1;
                    q.emplace(v);
                }
            }
        }
        return dist;
    }

    int chaseGame(vector<vector<int>>& edges, int startA, int startB) {
        n = edges.size();
        // 邻接表
        g.resize(n+1);
        vector<int> indeg(n+1);
        for (auto& e : edges) {
            g[e[0]].emplace_back(e[1]);
            g[e[1]].emplace_back(e[0]);
            // 如果他们两个可以直接到达，直接返回
            if ((e[0] == startA && e[1] == startB) || (e[0] == startA && e[1] == startB)) {
                return 1;
            }
            indeg[e[0]]++;
            indeg[e[1]]++;
        }

        auto a_all = bfs(startA);
        auto b_all = bfs(startB);

        // topo
        int loop = n;
        queue<int> q;
        for (int i = 1; i <= n; ++i) {
            if (indeg[i] == 1) q.emplace(i);
        }
        while (!q.empty()) {
            int f = q.front();
            q.pop();
            loop--;
            for (auto& v : g[f]) {
                indeg[v]--;
                if (indeg[v] == 1) {
                    q.emplace(v);
                }
            }
        }
        
        int ret = 1;
        if (loop <= 3) {
            for (int i = 1; i <= n; ++i) {
                if (a_all[i] > b_all[i] + 1) {
                    ret = max(a_all[i], ret);
                }
            }
        } else {
            for (int i = 1; i <= n; ++i) {
                if (a_all[i] > b_all[i] + 1) {
                    if (indeg[i] > 1) {
                        ret = -1;
                        break;
                    }
                    ret = max(a_all[i], ret);
                    
                }
            }
        }
        return ret;
    }
};




int main() {
    Solution sol;
    vector<vector<int>> edges = {{1,2},{2,3},{3,4},{4,1},{2,5},{5,6}};
    int s = sol.chaseGame(edges, 3, 5);
    cout << s << endl;
    return 0;
}