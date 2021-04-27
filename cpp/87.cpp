#include <bits/stdc++.h>

using namespace std;

int memory[31][31][31][31];

class Solution {
public:
    bool dfs(string s1, string s2, int l, int r, int x, int y) {
        if (memory[l][r][x][y] >= 0) return memory[l][r][x][y];
        int i = l, j = x;
        if (s1.substr(l, r-l+1) == s2.substr(x, y-x+1)) return memory[l][r][x][y] = 1;
        int n = r - l + 1;
        for (int i = 0; i < n-1; ++i) {
            if ((dfs(s1, s2, l, l+i, x, x+i) && dfs(s1, s2, l+i+1, r, x+i+1, y)) ||
                (dfs(s1, s2, l, l+i, y-i, y) && dfs(s1, s2, l+i+1, r, x, x + (r-l-i-1))) ) {
                    return memory[l][r][x][y] = 1;
            }

        }
        return memory[l][r][x][y] = 0;
        
    }
    bool isScramble(string s1, string s2) {
        memset(memory, -1, sizeof(memory));
        int n = s1.size();
        return dfs(s1, s2, 0, n-1, 0, n-1);
    }
};

int main() {
    Solution sol;
    cout << sol.isScramble("abcde", "caebd") << endl;
    return 0;
}
