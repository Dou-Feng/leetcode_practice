#include <iostream>
#include <vector>

using namespace std;


class Solution {
public:
    
    inline int f(int d, int l, int r) {
        if (d == 0) return l;
        d -= abs(r - l);
        return max(l, r) + d / 2;
    }
    int maxBuilding(int n, vector<vector<int>>& res) {
        int m = res.size();
        if (m == 0) return n-1;
        sort(res.begin(), res.end());
        int ret = 0;
        vector<int> h(m);
        int b = -1;
        for (int i = 0; i < m; ++i) {
            h[i] = min(res[i][1], res[i][0] + b);
            b = h[i] - res[i][0];
        }
        b = res[m-1][0] + h[m-1];
        for (int i = m-2; i >=0; --i) {
            h[i] = min(h[i], b - res[i][0]);
            b = res[i][0] + h[i];
        }
        for (int i = 0; i < m; ++i) {
            if (i == 0) {
                ret = f(res[i][0] - 1, 0, h[i]);
            } else {
                ret = max(ret, f(res[i][0] - res[i-1][0], h[i-1], h[i]));
            }
        }
        ret = max(ret, n - res[m-1][0] + h[m-1]);
        return ret;
    }
};