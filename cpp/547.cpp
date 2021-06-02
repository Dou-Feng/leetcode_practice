#include <bits/stdc++.h>

using namespace std;

class UF {
public:
    vector<int> parent;
    
    UF(int n) : parent(vector<int>(n)) {
        for (int i = 0; i < n; ++i) {
            parent[i] = i;
        }
    }

    int getParent(int x) {
        if (x != parent[x]) {
            parent[x] = getParent(parent[x]);
        }
        return parent[x];
    }

    void add(int u, int v) {
        int pu, pv;
        pu = getParent(u), pv = getParent(v);
        if (pu != pv) {
            parent[pu] = pv;
        }
    }
};

class Solution {
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        int n =  isConnected.size();
        UF uf(n);
        for (int i = 0; i < n; ++i) {
            for (int j = i+1; j < n; ++j) {
                if (isConnected[i][j])
                    uf.add(i, j);
            }
        }
        unordered_set<int> roots;
        for (int i = 0; i < n; ++i) {
            // cout << "i = " << i << ", p[i] = " << uf.getParent(i) << endl;
            roots.emplace(uf.getParent(i));

        }
        return roots.size();
    }
};

int main() {
    Solution sol;
    auto con = vector<vector<int>>({{1,0,0}, {0,1,0}, {0,0,1}});
    int s = sol.findCircleNum(con);
    cout << s << endl;
    return 0;
}