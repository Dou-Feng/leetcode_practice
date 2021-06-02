#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int m, n;
    int memory[31][31];
    bool dfs(string s, string p, int i, int j) {
        if (memory[i][j]) {
            return memory[i][j] == 1 ? 1 : 0;
        }
        if (i == m) {
            while (j < n) {
                if (j + 1 < n && p[j+1] == '*') j += 2;
                else break;
            }
            if (j == n) {
                memory[i][j] = 1;
                return true;
            } else {
                memory[i][j] = -1;
                return false;
            }
        }
        bool ans = false;
        // if p[j] == '*'
        
        
        if (j + 1 < n && p[j+1] == '*') {
            // 不需要这个符号
            ans = dfs(s, p, i, j+2);
            if (!ans && (p[j] == '.' || s[i] == p[j])) {
                ans = dfs(s, p, i+1, j);
            }
        } else {
            if (p[j] == '.' || s[i] == p[j]) {
                ans = dfs(s, p, i+1, j+1);
            } else {
                ans = false;
            }
        }
        if (ans) {
            memory[i][j] = 1;
            // cout << "Search " << s.substr(i) << ", " << p.substr(j) << " = true" << endl;
            return true;
        } else {
            memory[i][j] = -1;
            // cout << "Search " << s.substr(i) << ", " << p.substr(j) << " = false" << endl;
            return false;
        }
    }

    bool isMatch(string s, string p) {
        memset(memory, 0, sizeof(memory));
        m = s.size(), n = p.size();
        return dfs(s, p, 0, 0);
    }
};


int main() {
    Solution sol;
    cout << sol.isMatch("abcaaaaaaabaabcabac"
,".*ab.a.*a*a*.*b*b*") << endl;
    return 0;
}