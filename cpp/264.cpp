#include <bits/stdc++.h>

using namespace std;


class Solution {
public:
    int nthUglyNumber(int n) {
        vector<long long> rank(1, 1);
        vector<long long> factor({2, 3, 5});
        int i = 0;
        while (rank.size() < 3 * n && i < rank.size()) {
            for (int k = 0; k < 3; ++k) {
                long long key = factor[k] * rank[i];
                auto index = lower_bound(rank.begin(), rank.end(), key);
                if (index != rank.end() && *index == key) continue;
                // cout << i << ", " << key << endl;
                rank.insert(index, key);
            }
            ++i;
        }
        return rank[n-1];
    }
};


int main() {
    Solution sol;
    int s = sol.nthUglyNumber(1000);
    cout << s << endl;
    return 0;
}