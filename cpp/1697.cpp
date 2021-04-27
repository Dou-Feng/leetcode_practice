#include <bits/stdc++.h>

using namespace std;

class UF {
public:
    vector<int> p;
    vector<int> value;
    UF(int n) : p(vector<int>(n, 0)), value(vector<int>(n, 1)) {
        for (int i = 0; i < n; i++) {
            p[i] = i;
        }
    }

    int getRoot(int x) {
        if (x != p[x]) p[x] = getRoot(p[x]);
        return p[x];
    }

    void add(int u, int v) {
        int rootu = getRoot(u), rootv = getRoot(v);
        if (rootu == rootv) {
            return;
        }
        if (value[rootu] < value[rootv]) swap(rootu, rootv);
        if (rootu != rootv) {
            p[rootu] = rootv;
            value[rootv] += value[rootu];
        }
    }

    bool isConnected(int u, int v) {
        return getRoot(u)  == getRoot(v);
    }
};

class Solution {
public:
    vector<bool> distanceLimitedPathsExist(int n, vector<vector<int>>& edgeList, vector<vector<int>>& queries) {
        vector<int> qid(queries.size());
        iota(qid.begin(), qid.end(), 0);
        sort(qid.begin(), qid.end(), [&](int i, int j) {
            return queries[i][2] < queries[j][2];
        });

        sort(edgeList.begin(), edgeList.end(), [](vector<int> a, vector<int> b) {
            return a[2] < b[2];
        });

        UF uf(n);
        int j = 0;
        int en = edgeList.size();
        vector<bool> ret(queries.size(), false);
        for (auto i : qid) {
            vector<int> q = queries[i];
            while (j < en && q[2] > edgeList[j][2]) {
                uf.add(edgeList[j][0], edgeList[j][1]);
                j++;
            }
            ret[i] = uf.isConnected(q[0], q[1]);
        }

        return ret;
    }
};


int main() {
    Solution sol;
    vector<int> input({1, 2, 2, 3});
    vector<vector<int>> edges({{0,1,10}, {1,2,5}, {2,3,9}, {3,4,13}});
    vector<vector<int>> queries({{0,4,14}, {1,4,13}});
    // vector<vector<int>> edges({{0,1,2},{1,2,4},{2,0,8},{1,0,16}});
    // vector<vector<int>> queries({{0,1,2},{0,2,5}});
    vector<bool> s = sol.distanceLimitedPathsExist(5, edges, queries);
    for (auto e : s) {
        cout << e << ", ";
    }
    cout << endl;
    return 0;
}