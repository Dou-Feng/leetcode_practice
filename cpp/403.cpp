#include <bits/stdc++.h>

using namespace std;


// dp[i][j] 代表所处的位置为 i，当前的速度为 j 个单位，转移方程可以写成：
// dp[i][j] = dp[i-(j+1)][j+1] | dp[i-j][j] | dp[i-(j-1)][j-1]
class Solution {
public:
    bool canCross(vector<int>& stones) {
        unordered_map<int, int> sl;
        sl[0] = 0;
        for (int i = 1; i < stones.size(); ++i) {
            sl[stones[i]] = i;
            if (stones[i] - stones[i-1] > i) return false;
        }
        int n = stones.size();
        vector<vector<int>> dp(n+1, vector<int>(n+1));
        dp[0][1] = true;
        int k;
        for (int i = 1; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                // 当前的速度为 j，那么可以从 j-1, j, j+1 转换过来
                if (sl.count(stones[i] - (j-1)) && j > 0) {
                    k = sl[stones[i]-(j-1)];
                    dp[i][j] |= dp[k][j-1];
                }
                if (sl.count(stones[i] - j)) {
                    k = sl[stones[i]-j];
                    dp[i][j] |= dp[k][j];
                }
                if (sl.count(stones[i] - (j+1))) {
                    k = sl[stones[i] - (j+1)];
                    dp[i][j] |= dp[k][j+1];
                }
                if (i == n-1 && dp[i][j]) return true;
            }
        }
        return false;
    }
};

int main() {
    Solution sol;
    vector<int> input(2005);
    freopen("data.in", "r", stdin);
    int i = 0;
    while (!cin.eof()) {
        cin >> input[i++];
        // cout << input[i-1] << " ";
        // if (i % 100 == 0) cout << endl;
    }
    // cout << i << ", " << i << endl;
    input.resize(i);
    clock_t c = clock();
    bool s = sol.canCross(input);
    cout << s << endl;
    cout << clock() - c << endl;
    return 0;
}
