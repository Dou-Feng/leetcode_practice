#include <bits/stdc++.h>

using namespace std;

struct node {
    int children[26];
    bool isEnd;
    int depth;
    int fail;
}trie[600005];

class Solution {
public:
    int MAX_SIZE = 0;
    bool dp[1005];
    void add(string t) {
        // cout << "add, " << t << endl;
        int p = 0;
        int d = 0;
        for (auto& e : t) {
            if (trie[p].children[e - 'a'] == 0) {
                trie[p].children[e - 'a'] = ++MAX_SIZE;
            }
            p = trie[p].children[e - 'a'];
            ++d;
        }
        trie[p].isEnd = true;
        trie[p].depth = d;
    }

    void getFail() {
        queue<int> q;
        for (int i = 0; i < 26; ++i) {
            if (trie[0].children[i]) {
                trie[0].fail = 0;
                q.push(trie[0].children[i]);
            }
        }

        while (!q.empty()) {
            int now = q.front(); q.pop();

            for (int i = 0; i < 26; ++i) {
                if (trie[now].children[i]) {
                    trie[trie[now].children[i]].fail = trie[trie[now].fail].children[i];
                    q.push(trie[now].children[i]);
                } else {
                    trie[now].children[i] = trie[trie[now].fail].children[i];
                }
            }
        }
    }

    bool search(string& s) {
        if (s.size() == 0) return false;
        // cout << "search for " << s << endl;
        for (int i = 1; i <= s.size(); ++i) {
            dp[i] = false;
        }
        dp[0] = 1;
        // vector<bool> vis(MAX_SIZE+1, false);
        int res = 0, u = 0;
        for (int i = 0; i < s.size(); ++i) {
            u = trie[u].children[s[i] - 'a'];
            // cout << u << ", substr " << s.substr(0, i+1) << endl;
            for (int j = u; j; j = trie[j].fail) {
                // 如果刚好是本身，不能够算匹配
                if (trie[j].depth == s.size()) continue;
                // 当前 S[:i+1] 字符串的后缀存在，并且，前缀部分在之前的搜索当中已经被确定可以匹配
                // cout << trie[j].isEnd << ", " << trie[j].depth << endl;
                if (trie[j].isEnd && dp[i+1 - trie[j].depth]) {
                    // cout << "dp[" << i+1 << "] = 1" << endl;
                    dp[i+1] = 1;
                    break;
                }
            }
        }
        // cout << endl;
        return dp[s.size()];
    }

    vector<string> findAllConcatenatedWordsInADict(vector<string>& words) {
        memset(trie, 0, sizeof(trie));
        for (auto& e : words) {
            add(e);
        }
        getFail();
        vector<string> ret;
        dp[0] = true;
        // cout << "1" << endl;
        for (auto& e : words) {
            if (search(e)) {
                ret.push_back(e);
                // cout << "add " << e << endl;
            }
        }
        // cout << "2" << endl;
        return ret;
    }
};

vector<string> sparse(string& s) {
    vector<string> ret;
    int i = 0;
    while (i < s.size()) {
        if (s[i] == '\"') {
            int j = i + 1;
            while (s[j] != '\"') ++j;
            ret.push_back(s.substr(i+1, j - i - 1));
            i = j + 1;
        } else {
            ++i;
        }
    }
    return ret;
}

#define CASE 1

int main() {
    Solution sol;
#if CASE == 1
    ifstream ifs("472.input");
    string s;
    ifs >> s;
    vector<string> input = sparse(s);
    
    cout << input.size() << endl;
    vector<string> res = sol.findAllConcatenatedWordsInADict(input);
    
    ifstream ifs2("472_2.input");
    string s2;
    ifs2 >> s2;
    vector<string> gt = sparse(s2);
    sort(gt.begin(), gt.end());
    sort(res.begin(), res.end());
    for (int i = 0; i < gt.size(); ++i) {
        if (gt[i] != res[i]) {
            cout << gt[i] << ", " << res[i] << endl;
            return 0;
        }
    }
    cout << res.size() << ", " << gt.size() << endl;
    if (gt.size() != res.size()) {
        cout << "Fail!" << endl;
        return 0;
    }
    for (int i = 0; i < gt.size(); ++i) {
        if (gt[i] != res[i]) {
            
            cout << "Fail!" << endl;
            return 0;
        }
    }
    cout << "Success!" << endl;
#elif CASE == 2
    vector<string> input({"cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"});
    vector<string> res = sol.findAllConcatenatedWordsInADict(input);
    for (auto & e : res) {
        cout << e << ", ";
    }
    cout <<endl;
#endif
    return 0;
}