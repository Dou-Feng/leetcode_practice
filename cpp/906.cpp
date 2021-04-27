#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    inline int dup(int t, bool odd = true) {
        int sum = t;
        if (odd) t /= 10;
        while (t) {
            sum = sum * 10 + t % 10;
            t /= 10;
        }
        return sum;
    }
    inline bool isPalin(long long mul) {
        long long tmp = mul;
        long long sum = 0;
        while (tmp) {
            sum = sum * 10 + tmp % 10;
            tmp /= 10;
        }
        // cout << mul << ", " << sum << endl;
        return sum == mul;
    }

    int superpalindromesInRange(string left, string right) {
        long long L = atoll(left.c_str()), R = atoll(right.c_str());
        int MAGIC = 100000;
        
        int ret = 0;
        
        // odd
        for (int k = 1; k < MAGIC; ++k) {
            int c = dup(k);
            long long mul = 1ll * c * c;
            if (mul > R) break;
            if (mul >= L && isPalin(mul)) {
                cout << c << ", " << mul << endl;
                ++ret;
            }
        }

        for (int k = 1; k < MAGIC; ++k) {
            int c = dup(k, false);
            long long mul = 1ll * c * c;
            if (mul > R) break;
            if (mul >= L && isPalin(mul)) {
                cout << c << ", " << mul << endl;
                ++ret;
            }
        }
        return ret;
    }
};


int main() {
    Solution sol;
    cout << sol.superpalindromesInRange("4", "12312") << endl;
    return 0;
}