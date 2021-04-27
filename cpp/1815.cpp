#include <bits/stdc++.h>

using namespace std;

int freq0[9], freq[9], f[300000], w[9];

class Solution {
public:
    int maxHappyGroups(int b, vector<int>& groups) {
        int n = groups.size();
        memset(freq0, 0, sizeof(freq0));
        memset(f, 0, sizeof(f));
        for (int i = 0; i < n; ++i) {
            freq0[groups[i] % b]++;
        }
        int mmsum = 1;
        for (int i = 1; i < b; ++i) {
            mmsum *= (freq0[i] + 1);
        }
        w[1] = 1;
        for (int i = 2; i < b; ++i) {
            w[i] = w[i-1] * (freq0[i-1] + 1);
        } 
        for (int mask = 0; mask < mmsum; ++mask) {
            int last = 0;
            for (int i = 1; i < b; ++i) {
                freq[i] = (mask / w[i]) % (freq0[i] + 1);
                last = (last + freq[i] * i) % b;
            }

            for (int i = 1; i < b; ++i) {
                if (freq0[i] > freq[i])
                    f[mask + w[i]] = max(f[mask + w[i]], f[mask] + (last == 0));
            }
        }

        return freq0[0] + f[mmsum-1];
    }
};

int main() {
    Solution sol;
    vector<int> input({1,3,2,5,2,2,1,6});
    int s = sol.maxHappyGroups(4 , input);
    cout << s << endl;
    return 0;
}