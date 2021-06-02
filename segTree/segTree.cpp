#include <iostream>
#include <vector>
#include <string.h>

using namespace std;

#define MAX 1000005

#define IOS std::ios::sync_with_stdio(false); std::cin.tie(0);

struct Node {
    int sum;
    int l, r;
    Node() : sum(0), l(0), r(0) {}
};

int n, m;
Node tree[MAX << 1];

void build(int i, int l, int r) {
    if (l == r) {
        tree[i].l = tree[i].r = l;
        return;
    }
    tree[i].l = l, tree[i].r = r;
    int mid = l + ((r - l) >> 1);
    build(2*i, l, mid);
    build(2*i+1, mid+1, r);
}

void add(int i, int x, int v) {
    tree[i].sum += v;
    if (tree[i].l == tree[i].r) return;
    if (tree[2*i].r >= x) {
        add(2*i, x, v);
    } else {
        add(2*i+1, x, v);
    }
}

int query(int i, int l, int r) {
    if (tree[i].l >= l && tree[i].r <= r) {
        return tree[i].sum;
    }
    int ret = 0;
    if (tree[2*i].r >= l) {
        ret += query(2*i, l, r);
    }
    if (tree[2*i+1].l <= r) {
        ret += query(2*i+1, l, r);
    }
    return ret;
}


int main() {
    IOS
    memset(tree, 0, sizeof(tree));
    cin >> n >> m;
    build(1, 1, n);
    int t;
    for (int i = 1; i <= n; ++i) {
        cin >> t;
        add(1, i, t);
    }
    
    int op, x, y;
    while (m--) {
        cin >> op >> x >> y;
        if (op == 1) {
            add(1, x, y);
        } else {
            cout << query(1, x, y) << endl;
        }
    }
    return 0;
}