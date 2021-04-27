/*
 * @lc app=leetcode.cn id=399 lang=cpp
 *
 * [399] 除法求值
 */

// @lc code=start
#include <bits/stdc++.h>
#define MAX_SIZE 100

using namespace std;

// class UD {
// public:
//     vector<int> parent = vector<int>(MAX_SIZE, 0);
//     vector<double> values = vector<double>(MAX_SIZE, 1.0);
//     int size = 0;

//     UD(int n) {
//         size = n;
//         for (int i = 0; i < n; ++i) {
//             parent[i] = i;
//         }
//     }

//     int getParent(int x) {
//         if (x != parent[x]) {
//             int pre = parent[x];
//             parent[x] = getParent(parent[x]);
//             // update the value
//             values[x] *= values[pre];
//         }
//         return parent[x];
//     }
    
//     void add(int u, int v, double e) {
//         int pu, pv;
//         pu = getParent(u);
//         pv = getParent(v);
        
//         if (pu != pv) {
//             parent[pu] = pv;
//             values[pu] = e * values[v] / values[u];
//         }
//     }

//     bool isConnected(int u, int v) {
//         return getParent(u) == getParent(v);
//     }

//     double getAns(int u, int v) {
//         if (isConnected(u, v)) {
//             return values[u] / values[v];
//         }
//          return -1.0;
//     }
// };

// class Solution {
// public:
//     vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
//         unordered_map<string, int> nos;
//         int no = 0;
//         for (auto line : equations) {
//             if (nos.find(line[0]) == nos.end()) {
//                 nos[line[0]] = no++;
//             }
//             if (nos.find(line[1]) == nos.end()) {
//                 nos[line[1]] = no++;
//             }
            
//         }
//         UD ud(no);
//         for (int i = 0; i < equations.size(); ++i) {
//             int u, v;
//             u = nos[equations[i][0]];
//             v = nos[equations[i][1]];
//             ud.add(u, v, values[i]);
//         }

//         vector<double> ans;
//         for (auto pa : queries) {
//             int u, v;
//             u = nos[pa[0]];
//             v = nos[pa[1]];
//             ans.push_back(ud.getAns(u, v));
//         }
//         return ans;
//     }
// };
class Solution {
public:
    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        unordered_map<string, int> nos;
        vector<vector<pair<int, double>>> graph(100, vector<pair<int, double> >());
        int no = 0;
        for (int i = 0; i < equations.size(); ++i) {
            auto line = equations[i];
            if (nos.find(line[0]) == nos.end()) {
                nos[line[0]] = no++;
            }
            if (nos.find(line[1]) == nos.end()) {
                nos[line[1]] = no++;
            }
            graph[nos[line[0]]].push_back( make_pair(nos[line[1]], values[i]) );
            graph[nos[line[1]]].push_back( make_pair(nos[line[0]], 1 / values[i]));
        }
        
        vector<double> res;

        for (auto q : queries) {
            if (nos.find(q[0]) != nos.end() && nos.find(q[1]) != nos.end()) {
                queue<pair<int, double> > que;
                vector<bool> valid(no, true);
                // 如果起点和终点相同
                if (nos[q[0]] == nos[q[1]]) {
                    res.push_back(1.0);
                    continue;
                }
                que.push(make_pair(nos[q[0]], 1.0));
                valid[nos[q[0]]] = false;
                bool igotcha = false;
                while (que.size() && !igotcha) {
                    auto front = que.front();
                    int fno = front.first;
                    double value = front.second;
                    for (int i = 0; i < graph[fno].size(); ++i) {
                        auto pa = graph[fno][i];
                        // 遍历过直接跳过
                        if (valid[pa.first] == false) {
                            continue;
                        }
                        if (pa.first == nos[q[1]]) {
                            res.push_back(value * pa.second);
                            igotcha = true;
                            break;
                        }
                        que.push(make_pair(pa.first, value * pa.second));
                        valid[pa.first] = false;
                        
                    }
                    if (!igotcha)
                        que.pop();
                }
                if (que.size() == 0) {
                    res.push_back(-1.0);
                }
            } else {
                res.push_back(-1.0);
            }
        }
        return res;
        
        
    }
};
// @lc code=end

