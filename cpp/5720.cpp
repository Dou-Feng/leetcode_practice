#include <bits/stdc++.h>

using namespace std;

using ll = long long;

class Solution {
public:
    int mod = 1000000007;
    inline int myPow(int x, int p) {
        // cout << x << ", " << p << ", ";
        int res = 1;
        for (; p; p >>= 1) {
            if (p & 0x1) res = 1ll * res * x % mod;
            x = 1ll * x * x % mod;
        }
        // cout <<  res << endl;
        return res;

    }

    inline int inv(int x) {
        return myPow(x, mod - 2);
    }

    int makeStringSorted(string s) {
        int n = s.size();
        // 根据费马小定理 a_1 = a^{mod - 2}
        int fac[3005];
        fac[0] = 1;
        for (int i = 1; i < n; ++i) {
            fac[i] = (1ll * fac[i-1] * i) % mod;
            // cout << i << ", " << fac[i] << ", " << infac[i] << endl;
        }
        int freq[26];
        memset(freq, 0, sizeof(freq));
        ll ans = 0;
        for (int i = n-1; i >= 0; --i) {
            ++freq[s[i] - 'a'];
            int rank = 0;
            for (int j = 0; j < s[i] - 'a'; ++j) {
                rank += freq[j];
            }
            int cur = 1ll * rank * fac[n - i - 1] % mod;
            int dome = 1;
            for (int j = 0; j < 26; ++j) {
                dome = 1ll * dome * fac[freq[j]] % mod;
            }
            cur = 1ll * cur * inv(dome) % mod;
            // cout << inv(dome) << ", " << cur << endl;
            ans = (ans + cur) % mod;
        }
        return ans;
    }
};



int main() {
    Solution sol;
    cout << sol.makeStringSorted("leetcodeleetcodeleetcode") << endl;
    return 0;
}