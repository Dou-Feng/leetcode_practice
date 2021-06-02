#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;

#define MAX_SIZE 1000007
ll seq[MAX_SIZE];
ll tree[MAX_SIZE];

class BIT {
public:
    ll n;

    int lowbit(int x) {
        return x & (-x);
    }

    BIT(ll n, ll * seq) : n(n) {
        for (int i = 1; i <= n; ++i) {
            tree[i] += seq[i-1];
            int j = i + lowbit(i);
            if (j <= n) {
                tree[j] += tree[i];
            }
        }
    }

    void add(int i, ll x) {
        while (i <= n) {
            tree[i] += x;
            i += lowbit(i);
        }
    }

    ll query(int i) {
        ll ret = 0;
        while (i) {
            ret += tree[i];
            i -= lowbit(i);
        }
        return ret;
    }

    ll query(int l, int r) {
        return query(r) - query(l - 1);
    }
};

int main(void) {
    ll n, q;
    cin >> n >> q;
    for (int i = 0; i < n; ++i) {
        cin >> seq[i];
    }
    BIT bit(n, seq);
    while (q) {
        ll op, x, y;
        cin >> op >> x >> y;
        if (op == 1) {
            bit.add(x, y);
        } else {
            cout << bit.query(x, y) << endl;
        }
        q -= 1;
    }
    return 0;
}