#include <bits/stdc++.h>

using namespace std;



class Solution {
public:
    int numDistinct(string s, string t) {
        int m = s.size();
        int n = t.size();
        if (m < n || n == 0) {
            return 0;
        }
        auto dp = vector<int>(n+1, 0);
        dp[0] = 1;
        for (int i = 1; i <= m; ++i) {
            auto cpy = dp;
            for (int j = 1; j <= i && j < n+1; ++j) {
                if (s[i-1] == t[j-1]) dp[j] += cpy[j-1];
            }
        }

        return dp[n];
    }
};

int main() {
    Solution sol;
    // vector<int> input({1, 2, 2, 3});
    int s = sol.numDistinct("babgbag", "bag");
    cout << s << endl;
    return 0;
}