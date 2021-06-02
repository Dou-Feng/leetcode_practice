#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int maxWidthRamp(vector<int>& nums) {
        // 我们需要保存小于等于 nums[j] 的元素，然后找到这些元素中下标最小的
        vector<int> index(nums.size());
        iota(index.begin(), index.end(), 0);
        sort(index.begin(), index.end(), [&](auto& i, auto& j) {
            return nums[i] < nums[j] || (nums[i] == nums[j] && i < j);
        });
        int ret = 0, pre = 0x3f3f3f3f;
        for (int i = 0; i < nums.size(); ++i) {
            cout << "index = " << index[i] << ", value = " << nums[index[i]] << endl; 
            ret = max(ret, index[i] - pre);
            pre = min(pre, index[i]);
        }
        return ret;
    }
};


int main() {
    Solution sol;
    vector<int> input = {3,28,15,1,4,12,6,19,8,15,3,9,6,4,13,12,6,12,10,1,2,1,4,1,4,0,0,1,1,0};
    cout << sol.maxWidthRamp(input) << endl;
}