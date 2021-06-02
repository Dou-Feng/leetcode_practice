#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

class Solution {
public:
    int calculate(string s) {
        vector<int> stk;
        char preSign = '+';
        int num = 0;
        int n = s.length();
        for (int i = 0; i < n; ++i) {
            if (isdigit(s[i])) {
                num = num * 10 + int(s[i] - '0');
            }
            if (!isdigit(s[i]) && s[i] != ' ' || i == n-1) {
                switch (preSign)
                {
                case '+':
                    stk.push_back(num);
                    break;
                case '-':
                    stk.push_back(-num);
                    break;
                case '*':
                    stk.back() *= num;
                    break;
                default:
                    stk.back() /= num;
                    break;
                }
                preSign = s[i];
                num = 0;
            }
        }
        return accumulate(stk.begin(), stk.end(), 0);
    }
};

int main() {
    Solution sol;
    string input("2*3+4");
    int s = sol.calculate(input);
    cout << s << endl;

    // string input2(" 3/2 ");
    // s = sol.calculate(input2);
    // cout << s << endl;

    // string input3(" 3+5 / 2");
    // s = sol.calculate(input3);
    // cout << s << endl;
    return 0;
}