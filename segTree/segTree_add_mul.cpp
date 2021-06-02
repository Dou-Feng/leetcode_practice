#include <iostream>
#include <vector>
#include <string.h>

using namespace std;


// #define DEBUG


#define MAX 100005

#define IOS std::ios::sync_with_stdio(false); std::cin.tie(0);

using ll = long long;

struct Node {
    ll sum, plz, mlz;
    int l, r;
};


int n, m;
ll p;
Node tree[MAX << 2];

void build(int i, int l, int r) {
    tree[i].l = l, tree[i].r = r;
    tree[i].plz = 0, tree[i].mlz = 1, tree[i].sum = 0;
    if (l == r) return;
    int mid = l + ((r - l) >> 1);
    build(2*i, l, mid);
    build(2*i+1, mid+1, r);
}

void pushdown(int i) {
    int l = tree[i].l, r = tree[i].r;
    int mid = l + ((r - l) >> 1);
    ll k1 = tree[i].mlz, k2 = tree[i].plz;
    #ifdef DEBUG
    // cout << "Pushdown::" << l << ", " << r << endl;
    // cout << "k1, k2 = " << k1 << ", " << k2 << endl;
    #endif 
    tree[2*i].sum = (tree[2*i].sum * k1 + k2 * (mid - l + 1)) % p;
    tree[2*i+1].sum = (tree[2*i+1].sum * k1 + k2 * (r - mid)) % p;
    tree[2*i].mlz = (tree[2*i].mlz * k1) % p;
    tree[2*i+1].mlz = (tree[2*i+1].mlz * k1) % p;
    tree[2*i].plz = (tree[2*i].plz * k1 + k2) % p;
    tree[2*i+1].plz = (tree[2*i+1].plz * k1 + k2) % p;
    // reset
    tree[i].mlz = 1, tree[i].plz = 0;
}


void mul(int i, int l, int r, ll v) {
    // 如果包含这个区间，那么直接更新
    if (tree[i].l >= l && tree[i].r <= r) {
        tree[i].sum = (tree[i].sum * v) % p;
        tree[i].mlz = (tree[i].mlz * v) % p;
        tree[i].plz = (tree[i].plz * v) % p;
        #ifdef DEBUG
        cout << "Mul::seg::" << tree[i].l << ", " << tree[i].r << endl;
        cout << "times = " << v << ", result = " << tree[i].sum  << endl;
        #endif
        return;
    }
    pushdown(i);
    if (tree[2*i].r >= l) {
        mul(2*i, l, r, v);
    }
    if (tree[2*i+1].l <= r) {
        mul(2*i+1, l, r, v);
    }
    tree[i].sum = (tree[2*i].sum + tree[2*i+1].sum) % p;
}

void add(int i, int l, int r, ll v) {
    // 如果包含这个区间，那么直接更新
    if (tree[i].l >= l && tree[i].r <= r) {
        tree[i].sum = (tree[i].sum + (tree[i].r - tree[i].l + 1) * v) % p;
        tree[i].plz = (tree[i].plz + v) % p;
        #ifdef DEBUG
        cout << "Add::seg::" << tree[i].l << ", " << tree[i].r << endl;
        cout << "Enlarge size = " << v * (tree[i].r - tree[i].l + 1) << ", orginal = " << tree[i].sum - v * (tree[i].r - tree[i].l + 1) << endl;
        #endif
        return;
    }
    pushdown(i);
    if (tree[2*i].r >= l) {
        add(2*i, l, r, v);
    }
    if (tree[2*i+1].l <= r) {
        add(2*i+1, l, r, v);
    }
    tree[i].sum = (tree[2*i].sum + tree[2*i+1].sum) % p;
}


ll query(int i, int l, int r) {
    if (tree[i].l >= l && tree[i].r <= r) {
        return tree[i].sum;
    }
    pushdown(i);
    ll ret = 0;
    if (tree[2*i].r >= l) {
        ret = (ret + query(2*i, l, r)) % p;
    }
    if (tree[2*i+1].l <= r) {
        ret = (ret + query(2*i+1, l, r)) % p;
    }
    return ret;
}



int main() {
    IOS
    cin >> n >> m >> p;
    build(1, 1, n);
    ll t;
    for (int i = 1; i <= n; ++i) {
        cin >> t;
        add(1, i, i, t);
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
            mul(1, x, y, k);
            #ifdef DEBUG
            cout << "For debug: " << endl;
            for (int i = 1; i <= n; ++i) {
                cout << query(1, i, i) << ", ";
            }
            cout << endl;
            #endif
        } else if (op == 2) {
            cin >> x >> y >> k;
            add(1, x, y, k);
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