#include <iostream>
#include <vector>
#include <string.h>

using namespace std;

#define MAX 1000005

#define IOS std::ios::sync_with_stdio(false); std::cin.tie(0);

using ll = long long;

struct Node {
    ll sum, lz;
    int l, r;
    Node() : sum(0ll), l(0), r(0), lz(0ll) {}
};

int n, m;
Node tree[MAX << 1];

void build(int i, int l, int r) {
    tree[i].l = l, tree[i].r = r;
    if (l == r) return;
    int mid = l + ((r - l) >> 1);
    build(2*i, l, mid);
    build(2*i+1, mid+1, r);
}

void pushdown(int i) {
    int l = tree[i].l, r = tree[i].r;
    int mid = l + ((r - l) >> 1);
    if (tree[i].lz) {
        tree[2*i].lz += tree[i].lz;
        tree[2*i+1].lz += tree[i].lz;
        tree[2*i].sum += tree[i].lz * (mid - l + 1);
        tree[2*i+1].sum += tree[i].lz * (r - mid);
        tree[i].lz = 0;
    }
}

void up_seg(int i, int l, int r, ll v) {
    // 如果包含这个区间，那么直接更新
    if (tree[i].l >= l && tree[i].r <= r) {
        // cout << "Seg::" << tree[i].l << ", " << tree[i].r << endl;
        tree[i].sum += v * (tree[i].r - tree[i].l + 1);
        // cout << "Enlarge size = " << v * (tree[i].r - tree[i].l + 1) << ", orginal = " << tree[i].sum - v * (r - l + 1) << endl;
        tree[i].lz += v;
        return;
    }
    pushdown(i);
    if (tree[2*i].r >= l) {
        up_seg(2*i, l, r, v);
    }
    if (tree[2*i+1].l <= r) {
        up_seg(2*i+1, l, r, v);
    }
    tree[i].sum = tree[2*i].sum + tree[2*i+1].sum;
}


ll query(int i, int l, int r) {
    if (tree[i].l >= l && tree[i].r <= r) {
        return tree[i].sum;
    }
    pushdown(i);
    ll ret = 0;
    if (tree[2*i].r >= l) {
        ret += query(2*i, l, r);
    }
    if (tree[2*i+1].l <= r) {
        ret += query(2*i+1, l, r);
    }
    return ret;
}


// #define DEBUG


int main() {
    IOS
    memset(tree, 0, sizeof(tree));
    cin >> n >> m;
    build(1, 1, n);
    ll t;
    for (int i = 1; i <= n; ++i) {
        cin >> t;
        up_seg(1, i, i, t);
    }
    
    #ifdef DEBUG
    cout << "For debug: " << endl;
    for (int i = 1; i <= n; ++i) {
        cout << query(1, i, i) << ", ";
    }
    cout << endl;
    #endif
    int op, x, y;
    ll k;
    while (m--) {
        cin >> op;
        if (op == 1) {
            cin >> x >> y >> k;
            up_seg(1, x, y, k);
            #ifdef DEBUG
            cout << "For debug: " << endl;
            for (int i = 1; i <= n; ++i) {
                cout << query(1, i, i) << ", ";
            }
            cout << endl;
            #endif
        } else {
            cin >> x >> y;
            cout << query(1, x, y) << endl;
        }
    }
    return 0;
}