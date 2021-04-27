#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
  int n, m;
  int dx[4] = {1, -1, 0, 0};
  int dy[4] = {0, 0, 1, -1};
  
  bool inbound(int x, int y) {
    return x >= 0 && x < n && y >= 0 && y < m;
  }
  
  vector<vector<int> > bfs(int org_x, int org_y, vector<string>& maze) {
    queue<pair<int, int> > q;
    vector<vector<int> > ret(n, vector<int>(m, -1));
    // 把org初始点加入到队列中
    q.push(make_pair(org_x, org_y));
    // 初始化距离
    ret[org_x][org_y] = 0;

    int x, y;
    int nx, ny;
    while (!q.empty()) {
      x = q.front().first;
      y = q.front().second;
      q.pop();
      for (int k = 0; k < 4; k++) {
        nx = x + dx[k];
        ny = y + dy[k];
        if (inbound(nx, ny) && maze[nx][ny] != '#' && ret[nx][ny] == -1) {
          ret[nx][ny] = ret[x][y] + 1;
        //   cout << "BFS:" << "ret[" << nx << "][" << ny << "] = " << ret[nx][ny] << endl;
          q.push(make_pair(nx, ny));
        }
      }
    }
    return ret;
  }

  int minimalSteps(vector<string>& maze) {
    n = maze.size(), m = maze[0].size();
    vector<pair<int, int> > buttons, rocks;
    int sx, sy, tx, ty;
    // 初始化一些地图上的元素
    for (int i = 0; i < maze.size(); i++) {
      for (int j = 0; j < maze[i].size(); j++) {
        if (maze[i][j] == 'O') {
          rocks.push_back(make_pair(i, j));
        } else if (maze[i][j] == 'M') {
          buttons.push_back(make_pair(i, j));
        } else if (maze[i][j] == 'S') {
          sx = i;
          sy = j;
        } else if (maze[i][j] == 'T') {
          tx = i;
          ty = j;
        }
      }
    }

    // 求得开始点到任意点的距离sd
    vector<vector<int> > sd = bfs(sx, sy, maze);
    int nb = buttons.size();
    int ns = rocks.size();

    // 没有任何button的情况
    if (nb == 0) {
        // cout << "Ternimate of No button at all" << endl;
        return sd[tx][ty];
    }

    // 得到两个button之间的最短距离M->O->M`，dict[i][j] 表示button[i]->O->button[j]的最短距离
    vector<vector<int> > dict(nb, vector<int>(nb+2, -1));
    // 求得所有的M到任意点的距离
    vector<vector<vector<int> > > dd(nb);
    for (int i = 0; i < nb; i++) {
      dd[i] = bfs(buttons[i].first, buttons[i].second, maze);
      dict[i][nb+1] = dd[i][tx][ty];
    //   cout << "dict[" << i << "] = " << dict[i][nb+1] << endl;
    }

    for (int i = 0; i < nb; i++) {
        // 求得初始点到第一个button i的最小距离
        int tmp = -1;
        for (int k = 0; k < ns; k++) {
            int mid_x = rocks[k].first;
            int mid_y = rocks[k].second;
            // cout << "dd::" << i << " = " << dd[i][mid_x][mid_y] << endl;
            if (dd[i][mid_x][mid_y] == -1 || sd[mid_x][mid_y] == -1) continue;
            int path_len = sd[mid_x][mid_y] + dd[i][mid_x][mid_y];
            // cout << "path_len::(" <<  i << ", " << k << ") = " << path_len<< endl;
            if (tmp == -1 || path_len < tmp) {
                tmp = path_len;
            }
        }
        dict[i][nb] = tmp;

        // 求得button i 到button j的最小距离
        for (int j = i+1; j < nb; j++) {
            tmp = -1;
            for (int k  = 0; k < ns; k++) {
                int mid_x = rocks[k].first;
                int mid_y = rocks[k].second;
                if (dd[i][mid_x][mid_y] == -1 || dd[j][mid_x][mid_y] == -1) continue;
                int path_len = dd[i][mid_x][mid_y] + dd[j][mid_x][mid_y];
                if (tmp == -1 || path_len < tmp) {
                    tmp = path_len;
                }
            }
            dict[i][j] = tmp;
            dict[j][i] = tmp;
        }

    }
    // 无法达成的情形，有些button无法到达，或者终点无法到达
    for (int i = 0; i < nb; i++) {
        if (dict[i][nb] == -1 || dict[i][nb+1] == -1) {
            // cout << "Ternimate of the unreachable" << endl;
            return -1;
        }
    }
    // 初始化状态，利用二维数组来存储状态信息
    vector<vector<int> > dp((1 << buttons.size()), vector<int>(buttons.size(), -1));
    
    // 初始化dp
    for (int i = 0; i < nb; i++) {
        dp[1 << i][i] = dict[i][nb];
    }

    // 利用dp寻找使得路径最短的buttons顺序
    // 由于被改变的状态都大于原来的状态，而且被改变的状态改变之后不会再次发生变化，因此可以从小到大遍历
    for (int mask = 1; mask < (1 << nb); mask++) {
        for (int i = 0; i < nb; i++) {
            if (mask & (1 << i)) {
                for (int j = 0; j < nb; j++) {
                    if (!(mask & (1 << j))) {
                        int next = mask | (1 << j);
                        if (dp[next][j] == -1 || dp[next][j] > dp[mask][i] + dict[i][j]) {
                            dp[next][j] = dp[mask][i] + dict[i][j];
                        }
                    }
                }
            }
        }
    }

    // 从任意一个M到终点T，找到最短的那个状态
    int final_mask = (1 << nb) - 1;
    int ret = -1;
    for (int i = 0; i < nb; i++) {
        if (ret == -1 || ret > dp[final_mask][i] + dict[i][nb+1]) {
            ret = dp[final_mask][i] + dict[i][nb+1];
        }
    }

    return ret;
  }

  
};

int main() {
    Solution sol;
    vector<string> s;
    s.push_back("S#O");
    s.push_back("M..");
    s.push_back("M.T");
    cout << sol.minimalSteps(s) << endl;
}