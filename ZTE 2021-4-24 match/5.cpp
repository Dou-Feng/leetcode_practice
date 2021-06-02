#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <unordered_map>
#include <queue>
#include <unordered_set>
#include <memory.h>

using namespace std;

#define INF 0x3f3f3f3f
#define MAX 60005
#define BASE 20005

bool vis[MAX][2][16];

using tp32 = tuple<int, int, int>;

int s, t;
int choice[20];

int main() {
    int op = 1, step = 1, x;
    for (int i = 0; i <= 20; ++i) {
        choice[i] = (1 << i);
    }
    memset(vis, 0, sizeof(vis));
    cin >> s >> t;
    
    queue<tp32> q;
    q.push(make_tuple(s, 1, 0));
    int ans = 0;
    while (!q.empty()) {
        ++ans;
        int size = q.size();
        while (size--) {
            tp32 tp = q.front(); q.pop();
            x = get<0>(tp), op = get<1>(tp), step = get<2>(tp);

            // 重置
            if (!vis[x + BASE][1][0]) {
                q.push(make_tuple(x, 1, 0));
                vis[x + BASE][1][0] = 1;
            }

            // 选择跳跃
            int nxt = x + (op ? 1 : -1) * choice[step];
            if (nxt > 40000 || nxt < -20000) continue;
            if (nxt == t) {
                cout << ans << endl;
                return 0;
            }
            if (!vis[nxt + BASE][1-op][step+1]) {
                vis[nxt + BASE][1-op][step+1] = 1;
                q.push(make_tuple(nxt, 1-op, step+1));
            }
        }
    }

    return 0;
}