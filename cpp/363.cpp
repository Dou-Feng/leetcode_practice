#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int maxSumSubmatrix(vector<vector<int>>& matrix, int limit) {
        int ret = INT_MIN;
        set<int> sorted_list;
        
        int m = matrix.size(), n = matrix[0].size();
        for (int i = 0; i < n; ++i) {
            vector<int> org(m, 0);
            for (int j = i; j < n; ++j) {
                sorted_list.clear();
                for (int k = 0; k < m; ++k) {
                    org[k] += matrix[k][j];
                }
                int pre = 0;
                sorted_list.insert(pre);
                for (int k = 0; k < m; ++k) {
                    pre += org[k];
                    auto p = sorted_list.lower_bound(pre - limit);
                    sorted_list.insert(pre);
                    
                    if (p != sorted_list.end() && pre - (*p) <= limit) {
                        ret = max(ret, pre - (*p));
                    }
                }

                if (ret == limit) return limit;

            }
        }
        return ret;
    }
};


int main() {
    Solution sol;
    vector<vector<int>> input = {{5,-4,-3,4}, {-3,-4,4,5}, {5,1,5,-4}};
    cout << sol.maxSumSubmatrix(input, 10) << endl;
    return 0;
}