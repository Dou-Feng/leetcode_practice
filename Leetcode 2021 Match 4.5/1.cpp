#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int purchasePlans(vector<int>& nums, int target) {
        long long mod = 1000000007;
        long long ans = 0;
        sort(nums.begin(), nums.end());
        int n = nums.size();
        for (int i = 0; i < n-1; ++i) {
            auto j = upper_bound(nums.begin() + i + 1, nums.end(), target - nums[i]);
            ans = (ans + (j - nums.begin()) - i - 1) % mod;
        }
        return ans;
    }
};

int main() {
    // cout << "Hello, world" << endl;
    Solution sol;
    vector<int> input({2,2,1,9});
    cout << sol.purchasePlans(input, 10) << endl;
    return 0;
}