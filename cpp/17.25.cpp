#include <bits/stdc++.h>

using namespace std;
#define DEBUG

#define get(n, c) (trie[n].child[c - 'a'])
#define isend(n) (trie[n].end)
#define isnxt(n) (trie[n].nxt)

struct node {
    bool end, nxt;
    int child[26];
    node() {
        memset(child, 0, sizeof(child));
        end = nxt=  0;
    }
}trie[65000];

int N = 0;

void insert(string& w) {
    int p = 0;
    for (auto c : w) {
        if (!get(p, c)) {
            get(p, c) = ++N;
        }
        isnxt(p) = true;
        p = get(p, c);
    }
    isend(p) = true;
}

bool search(string& w) {
    int p = 0;
    for (auto c : w) {
        if (!get(p, c)) return false;
        p = get(p, c);
    }
    return isend(p);
}

inline bool allends(vector<int>& td) {
    for (auto& e : td) {
        if (!isend(e)) return false;
    }
    return true;
}

inline bool anynotnxt(vector<int>& td) {
    for (auto& e : td) {
        if (!isnxt(e)) return true;
    }
    return false;
}


class Solution {
public:
    // 记录最大面积和最终的答案
    int max_square = 0;
    vector<string> ret;
    // 记录单词长度为 i 的单词在数组中出现的范围
    vector<pair<int, int>> range;
    // 记录以 第 i 位 为字母 letter 的单词的最大长度
    vector<int> ltlen[105];

    // words 是可选的单词，而 ans 记录了 row 行已经满足要求的矩阵
    // 我们利用 td 记录 ans 中最后一行单词每个字母在字典树中所处的位置
    void backtrack(vector<string>& words, vector<string>& ans, vector<int>& td) {
        
        int row = ans.size();
        int col = ans.size() > 0 ? ans[0].size() : 0;
        #ifdef DEBUG
        cout << "backtrack, row = " << row << ", col = " << col << endl;
        for (auto& e : ans) cout << e << endl;
        #endif
        // 如果当前所有列都存在单词列表中，并且当前的矩阵大小比答案要大
        if (row * col > max_square && allends(td)) {
            max_square = row * col;
            ret = ans;
        }
        // 如果存在任何一个 p 到头了，直接返回
        // 枝剪1：由于我们是从大到小遍历单词，因此当 col == row 时，不再向下搜索
        if (row > 0 && (anynotnxt(td) || col == row)) return;

        // 枝剪2：每一行的长度一致的下标
        int st = range[col].first, en = range[col].second;
        #ifdef DEBUG
        cout << "Search range(" << st << ", " << en << ") " << endl;
        #endif
        for (int i = st; i < en; ++i) {
            auto& w = words[i];
            if (max_square >= w.size() * w.size()) break;
            // 判断是否能够加入到最后一行，
            // 要满足每一列的单词子串都存在于字典树中
            // 枝剪3：考虑添加一行时，需要考虑到是否有必要加入到最后, 
            vector<int> new_td(w.size());
            bool valid = true;
            int min_len = 1000;
            for (int i = 0; i < w.size(); ++i) {
                if (!get(td[i], w[i])) {
                    valid = false;
                    break;
                } else {
                    new_td[i] = get(td[i], w[i]);
                    min_len = min(min_len, ltlen[row][w[i] - 'a']);
                }
            }
            // 枝剪4：如果当前行添加上去的效果都不如原来的结果，直接舍去
            if (valid && (col == 0 || max_square < min_len * col)) {
                ans.emplace_back(w);
                backtrack(words, ans, new_td);
                ans.pop_back();
            }
        }
    }
        
    vector<string> maxRectangle(vector<string>& words) {
        memset(trie, 0, sizeof(trie));
        N = 0;
        ios::sync_with_stdio(false);
        cin.tie(nullptr);
        // 把 words 按照长度倒序排列
        sort(words.begin(), words.end(), [](auto& a, auto& b) {
            return a.size() > b.size();
        });

        // 初始化长度相同的单词在数组中出现的范围
        range.resize(105);
        int i = 0, l = 0;
        for (int i = 0; i < 105; ++i) {
            ltlen[i].resize(26);
        }
        for (int j = 0; j < words.size(); ++j) {
            for (int k = 0; k < words[j].size(); ++k) {
                ltlen[k][words[j][k] - 'a'] = max(ltlen[k][words[j][k] - 'a'], (int) words[j].size());
            }
            
            if (l != words[j].size()) {
                range[l] = make_pair(i, j);
                l = words[j].size();
                i = j;
            }
        }
        range[l] = make_pair(i, words.size());
        range[0] = make_pair(0, words.size());
        // 添加到字典树
        for (auto& w : words) insert(w);
        vector<string> tmp;
        vector<int> td(105);
        backtrack(words, tmp, td);
        // cout << N << endl;
        return ret;
    }
};

#define CASE 1

int main() {
    Solution sol;
    #if CASE == 1
    vector<string> words = {"this", "real", "hard", "trh", "hea", "iar", "sld"};
    #elif CASE == 2
    vector<string> words = {"aa", "aa"};
    #endif
    vector<string> ans = sol.maxRectangle(words);
    for (auto e : ans) {
        cout << e << endl;
    }
    cout << endl;
}