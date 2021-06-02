#include <bits/stdc++.h>

using namespace std;



class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int n = edges.size();
        vector<vector<int>> graph(n+1, vector<int>());
        for (auto elem : edges) {
            graph[elem[1]].push_back(elem[0]);
            graph[elem[0]].push_back(elem[1]);
        }

        for (auto iter = edges.rbegin(); iter != edges.rend(); iter++) {
            vector<int> elem = *iter;
            queue<int> que;
            que.push(1);
            vector<bool> valid(n+1, true);
            int cnt = 1;
            valid[1] = false;
            while (que.size()) {
                for (auto node : graph[que.front()]) {
                    // cout << "front " << que.front() << ", " << "node " << node << endl; 
                    if ((node == elem[0] && que.front() == elem[1]) || (node == elem[1] && que.front() == elem[0]) || !valid[node]) {
                        // cout << "skip edge " << elem[0] << ", " << elem[1] << endl;
                        continue;
                    }
                    valid[node] = false;
                    que.push(node);
                    cnt += 1;
                }
                que.pop();
            }
            if (cnt == n) {
                return elem;
            }
        }
        return {1, 1};
    }
};


int main() {
    Solution sol;
    // vector<vector<int>> input({{1,2}, {1,3}, {2,3}});
    vector<vector<int>> input({ {1,2}, {2,3}, {3,4}, {1,4}, {1,5} });
    vector<int> s = sol.findRedundantConnection(input);
    for (auto e : s) {
        cout << e << " ";
    }
    cout << endl;
    return 0;
}