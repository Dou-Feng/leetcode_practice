#include <bits/stdc++.h>

using namespace std;
using PII=pair<int, int>;

class Solution {
public:
    int storeWater(vector<int>& bucket, vector<int>& vat) {
        priority_queue<PII, vector<PII>, less<PII>> pq;
        int op = 0;
        for (int i = 0; i < bucket.size(); ++i) {
            if (vat[i] == 0) continue;
            if (bucket[i] == 0) {
                op++;
                bucket[i]++;
            }
            pq.push({(vat[i] + bucket[i] -1) / bucket[i], i});
        }
        if (pq.empty()) return 0;
        int cnt = pq.top().first;
        int ret = 10000000;
        while (!pq.empty() && cnt--) {
            PII f = pq.top(); pq.pop();
            // cout << f.first << ", " << op << endl;
            if (ret >= f.first + op) {
                ret = f.first + op;
            }
            op++;
            bucket[f.second]++;
            pq.push({(vat[f.second] + bucket[f.second] - 1) / bucket[f.second], f.second});
        }
        
        return ret;
    }
};


int main() {
    Solution sol;
    vector<int> bucket({9, 9});
    vector<int> vat({5000, 5000});
    cout << sol.storeWater(bucket, vat) << endl;
    return 0;
}