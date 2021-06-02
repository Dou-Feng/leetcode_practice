#include <bits/stdc++.h>

using namespace std;


class Solution {
public:
    string largestNumber(vector<int>& nums) {
        // for (auto &e : nums) cout << e << ", "; cout << endl;
        sort(nums.begin(), nums.end(), [](const int& a, const int& b) {
            long long x = 10, y = 10;
            while (x <= a) {
                x *= 10;
            }
            while (y <= b) {
                y *= 10;
            } 
            return a * y + b > b * x + a;
        });
        string ans;
        if (nums[0] == 0) return "0";
        for (int i = 0; i < nums.size(); ++i) {
            ans += to_string(nums[i]);
        }   
        return ans;
    }
};

int main() {
    Solution sol;
    vector<int> input({0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0});
    cout << sol.largestNumber(input) << endl;
}