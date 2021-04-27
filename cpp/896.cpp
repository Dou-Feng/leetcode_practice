#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    bool isMonotonic(vector<int>& A) {
        return false;
    }
};


int main() {
    Solution sol;
    vector<int> input({1, 2, 2, 3});
    bool s = sol.isMonotonic(input);
    cout << s << endl;
    return 0;
}