#include <bits/stdc++.h>

using namespace std;


class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        int n = prices.size();
        vector<int> buy(k+1, -1000000007);
        vector<int> sell(k+1, -1000000007);
        sell[0] = buy[0] = 0;
        int last_sell, now_sell;
        for (int i = 0; i < n; ++i) {
            last_sell = 0;
            for (int j = 1; j <= k; ++j) {
                now_sell = sell[j];
                sell[j] = max(sell[j], buy[j] + prices[i]);
                buy[j] = max(buy[j], last_sell - prices[i]);
                last_sell = now_sell;
            }
        }
        int res = 0;
        for (int i = 0; i <= k; ++i) {
            res = max(res, sell[i]);
        }
        return res;
    }
};


int main() {
    Solution sol;
    vector<int> input({3,2,6,5,0,3});
    int s = sol.maxProfit(2, input);
    cout << s << endl;
    return 0;
}