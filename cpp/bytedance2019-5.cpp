#include <bits/stdc++.h>

using namespace std;
#define INF 0x3f3f3f3f

// 经典旅行商问题
int N;
int graph[25][25];
int main() {
    cin >> N;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            cin >> graph[i][j];
        }
    }
    // 状态压缩 dp
    // 复杂度 O(n^2 * 2^N)
    vector<vector<int>> f(1 << N, vector<int>(N, INF));
    // 初始化
    f[0][0] = 0;
    for (int mask = 0; mask < (1 << N) - 1; ++mask) {
        for (int city = 0; city < N; ++city) {
            // 如果当前状态不可达，直接退出
            if (f[mask][city] == INF) continue;
            // 选择可达的城市
            for (int arv = 0; arv < N; ++arv) {
                // 不能够访问过
                if (!(mask & (1 << arv))) 
                    f[mask | (1 << arv)][arv] = min(f[mask | (1 << arv)][arv], f[mask][city] + graph[city][arv]);
            }
        }
    }
    cout << f[(1<<N)-1][0] << endl;
    return 0;
}