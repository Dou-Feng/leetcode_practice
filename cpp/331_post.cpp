#include <bits/stdc++.h>

using namespace std;


class Solution {
public:
    bool isValidSerialization(string preorder) {
        int diff = 1;
        int i = 0, n = preorder.size();
        while (i < n) {
            if (preorder[i] == ',') {
                i += 1;
            } else if (preorder[i] == '#') {
                diff -= 1;
                i += 1;
            } else {
                while (i < n  && isdigit(preorder[i++]));
                diff += 1;
                if (diff > 0) {
                    return false;
                }
            }
        }
        return diff == 0;
    }
};


int main() {
    Solution sol;
    string input("#,#,4");
    bool s = sol.isValidSerialization(input);
    cout << s << endl;
    return 0;
}