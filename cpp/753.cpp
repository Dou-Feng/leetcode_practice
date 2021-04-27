#include <bits/stdc++.h>
#include <unordered_set>
using namespace std;

class Solution {
public:
    unordered_set<int> seen;
    int k, high;
    string ans;
    void dfs(int cur) {
        for (int i = 0; i < k; ++i) {
            int node = cur * 10 + i;
            if (!seen.count(node)) {
                seen.emplace(node);
                dfs(node % high);
                ans += i + '0';
            }
        }
    }
    string crackSafe(int n, int k) {
        this->k = k;
        high = pow(10, n - 1);
        dfs(0);
        ans += string(n-1, '0');
        return ans;
    }
};


int main() {
    Solution sol;
    string s = sol.crackSafe(2, 2);
    cout << s << endl;
    return 0;
}