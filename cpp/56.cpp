#include <bits/stdc++.h>

using namespace std;



class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());
        vector<vector<int>> ans;
        int close = intervals[0][0];
        int far = intervals[0][1];
        for (auto e : intervals) {
            // cout << "elem: " << e[0] << ", " << e[1] << endl;
            if (e[0] > far) {
                ans.push_back(vector<int>({close, far}));
                close = e[0];
                far = e[1];
            } else {
                far = max(far, e[1]);
            }
        }
        ans.push_back(vector<int>({close, far}));
        return ans;
    }
};



int main() {
    Solution sol;
    vector<vector<int>> input({ {1,3},{2,6},{2,7},{15,18} });
    vector<vector<int>> s = sol.merge(input);
    for (auto v : s) {
        cout << v[0] << ", " << v[1] << endl;
    }
    return 0;
}