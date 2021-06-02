#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int orchestraLayout(int n, int x, int y) {
        long long ans;
        long long l;
        l = min(x , y);
        l = min(min((int)l, n-1-x), n-1-y);
        // cout << "layer = " << l << endl; 
        ans = ((n - 1) * l - l * (l-1)) % 9;
        ans = (4 * ans) % 9 - 1;
        // cout << "outer number = " << ans << endl;
        if (x == l) { ans = (ans + y - l + 1) % 9; }
        else if (y == n-1-l) {
            ans = (ans + n-1-2*l + x-l + 1) % 9;
        } else if (x == n-1-l) {
            ans = (ans + 2 * (n-1-2*l) + (n-1-l - y) + 1) % 9;
        } else {
            ans = (ans + 3 * (n-1-2*l) + (n-1-l - x) + 1) % 9;
        }
        return ans + 1;
    }
};

int main() {
    Solution sol;
    // cout << sol.orchestraLayout(5, 1, 4) << " "; 
    int n = 4;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cout << sol.orchestraLayout(n, i, j) << " ";       
        }
        cout << endl;
    }
    return 0;
}