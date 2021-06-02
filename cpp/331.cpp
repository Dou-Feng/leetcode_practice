#include <bits/stdc++.h>

using namespace std;



typedef long long ll;

class Solution {
public:

    bool isValidSerialization(string preorder) {
        int n = preorder.size();
        if (n == 0) {
            return false;
        }
        int slot = 1;
        int  i = 0;
        while (i < n && slot) {
            if (preorder[i] == ',' || preorder[i] == ' ') {
                i++;
            } else if (preorder[i] == '#') {
                slot -= 1;
                i += 1;
            } else {
                while (i < n && isdigit(preorder[i])) {
                    i += 1;
                }
                slot += 1;
            }
        }

        return slot == 0 && i == n;
    }


};


int main() {
    Solution sol;
    string input("");
    bool s = sol.isValidSerialization(input);
    cout << s << endl;
    return 0;
}