#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;

#define MAX_SIZE 1000007

class BIT {
public:
    vector<ll> tree;
    int n;

    int lowbit(int x) {
        return x & (-x);
    }

    BIT(int n, int * seq) : n(n) {
        tree.resize(n+1);
        for (int i = 1; i <= n; ++i) {
            cout << "tree[" << i << "] = " << tree[i] << endl;
            tree[i] += seq[i-1];
            if (i + lowbit(i) <= n) {
                tree[i+lowbit(i)] += seq[i-1];
            }
        }
    }

    void add(int i, int x) {
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
    std::cout << "hello world" << std::endl;
    int n, q;
    cin >> n >> q;
    int seq[MAX_SIZE];
    for (int i = 0; i < n; ++i) {
        cin >> seq[i];
    }
    BIT bit(n, seq);
    while (q) {
        int op, x, y;
        cin >> op >> x >> y;
        cout << op << ", " << x << ",", y;
        if (op == 1) {
            bit.add(x, y);
        } else {
            cout << bit.query(x, y) << endl;
        }
        q -= 1;
    }
    return 0;
}