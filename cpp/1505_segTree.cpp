#include <bits/stdc++.h>

using namespace std;

#define MSIZE 30005

struct node {
    int l, r;
    int v;
    int lz;
} segTree[MSIZE << 2];

void build(int i, int l, int r) {
    // cout << i << ", " << l << ", " << r << endl;
    segTree[i].l = l;
    segTree[i].r = r;
    segTree[i].v = segTree[i].lz = 0;
    if (l < r) {
        int mid = (l + r) >> 1;
        build(i<<1, l, mid);
        build(i<<1|1, mid+1, r);
    }
}

// 下传 lazy tag
void pushdown(int i) {
    int tag = segTree[i].lz;
    if (tag) {
        segTree[i<<1].lz += tag;
        segTree[i<<1|1].lz += tag;
        segTree[i<<1].v += tag * (segTree[i<<1].r - segTree[i<<1].l + 1);
        segTree[i<<1|1].v += tag * (segTree[i<<1|1].r - segTree[i<<1|1].l + 1);
        segTree[i].lz = 0;
    }
}

void pushup(int i) {
    segTree[i].v = segTree[i<<1].v + segTree[i<<1|1].v;
}

// 区间修改，单点查询
void modify(int i, int l, int r, int v) {
    if (l > r) return ;
    if (segTree[i].l >= l && segTree[i].r <= r) {
        segTree[i].v += v * (segTree[i].r - segTree[i].l + 1);
        segTree[i].lz += v;
        return;
    }
    pushdown(i);
    // 如果左子结点与区间有交集
    if (segTree[i<<1].r >= l) {
        modify(i<<1, l, r, v);
    }
    if (segTree[i<<1|1].l <= r) {
        modify(i<<1|1, l, r, v);
    }
    pushup(i);
    // cout << "Cur node " << i << " seg [" << segTree[i].l << ", " << segTree[i].r << "] = " << segTree[i].v << endl;
}

// 区间修改，单点查询
int find(int i, int l, int r) {
    if (l > r) return 0;
    if (segTree[i].l >= l && segTree[i].r <= r) {
        return segTree[i].v;
    }
    pushdown(i);
    int res = 0;
    // 如果左子结点与区间有交集
    if (segTree[i<<1].r >= l) {
        res += find(i<<1, l, r);
    }
    if (segTree[i<<1|1].l <= r) {
        res += find(i<<1|1, l, r);
    }
    // pushup(i);
    return res;
}

class Solution {
public:
    string minInteger(string num, int k) {
        vector<queue<int>> rank(10);
        for (int i = 0; i < num.size(); ++i) {
            rank[num[i] - '0'].push(i);
        }
        int n = num.size();
        build(1, 0, n-1);
        string ret;
        for (int i = 0; i < num.size(); ++i) {
            for (int j = 0; j < 10; ++j) {
                if (rank[j].empty()) continue;
                int f = rank[j].front();
                int t = f - i + find(1, f, f);
                // cout << "(" << f << ", " << f << "), " << find(1, f, f) << endl;
                if (t <= k) {
                    // cout << "num = " << j << " at " << f << ", t = " << t << endl;
                    k -= t;
                    ret += to_string(j);
                    // cout << to_string(j) << ", " << ret << endl;
                    // 修改区间的值
                    modify(1, 0, f, 1);
                    rank[j].pop();
                    break;
                }
            }
        }

        return ret;
    }
};


int main() {
    Solution sol;
    cout << sol.minInteger("294984148179", 11) << endl;
    return 0;
}








#ifdef TEST

void pure_modify(vector<int>& arr, int l, int r, int v) {
    for (int i = l; i <= r; ++i) {
        arr[i] += v;
    }
}

void print(vector<int>& arr) {
    for (auto& e : arr) cout << e << " "; cout << endl;
}

int main() {
    int n = 100;
    vector<int> arr(n);
    iota(arr.begin(), arr.end(), 1);
    cout << "Orginal " << endl;
    print(arr);
    build(1, 0, n-1);
    for (int i = 0; i < n; ++i) {
        modify(1, i, i, arr[i]);
    }
    srand(0);
    // find(1, 9, 10);
    cout << "Seg search" << endl;
    int test_cases = 1000;
    while (test_cases--) {
        int v = rand() % 10000;
        int l = rand() % n, r = rand() % n;
        if (l > r) continue;
        // cout << "l, r, v = " << l << ", " << r << ", " << v << endl;
        modify(1, l, r, v);
        pure_modify(arr, l, r, v);
        // print(arr);
        int ans = find(1, l, r);
        int gd = accumulate(arr.begin() + l, arr.begin() + r + 1, 0);
        // cout << "seg [" << l << ", " << r << "] = " << ans << ", " << gd << endl;
        assert(ans == gd);
    }
    cout << "Success" << endl;
    return 0;
}
#endif