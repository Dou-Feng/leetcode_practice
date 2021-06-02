#include <iostream>
#include <vector>
#include <string.h>

using namespace std;

#define MAX 500005

#define IOS std::ios::sync_with_stdio(false); std::cin.tie(0);

int m, n;
int arr[MAX];
int tree[MAX];

int lowbit(int x) { return x&(-x); }

void build() {
    for (int i = 1; i <= n; ++i) {
        tree[i] += arr[i];
        int p = i + lowbit(i);
        if (p <= n) {
            tree[p] += tree[i];
        }
    }
}

void add(int x, int v) {
    while (x <= n) {
        tree[x] += v;
        x += lowbit(x);
    }
}

int query(int i) {
    int ret = 0;
    while (i) {
        ret += tree[i];
        i -= lowbit(i);
    }
    return ret;
}

int query(int l, int r) {
    return query(r) - query(l-1);
}

int main() {
    IOS
    memset(tree, 0, sizeof(tree));
    cin >> n >> m;
    for (int i = 1; i <= n; ++i) {
        cin >> arr[i];
    }
    build();
    int op, x, y;
    while (m--) {
        cin >> op >> x >> y;
        if (op == 1) {
            add(x, y);
        } else {
            cout << query(x, y) << endl;
        }
    }
    return 0;
}