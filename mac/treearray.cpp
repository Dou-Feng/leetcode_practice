#include <iostream>
using namespace std;

typedef long long ll;
ll nums[1000006];
int n, q;
int l, r, i;
ll x;
int op;
ll cur, last;
int lowbit(int x) {return x&(-x);}

void add(int i, ll x) {
    while (i <= n) {
        nums[i] += x;
        i += lowbit(i);
    }
}
void insert(int l, int r, ll x) {
    add(l, x);
    add(r+1, -x);
}

ll get(int i) {
    ll res = 0;
    while (i) {
        res += nums[i];
        i -= lowbit(i);
    }
    return res;
}

int main() {
    cin >> n >> q;
    for (int i = 1; i <= n; ++i) {
        cin >> cur;
        nums[i] += cur - last;
        int j = i + lowbit(i);
        if (j <= n) {
            nums[j] += nums[i];
        }
        last = cur;
    }
    
    while (q--) {
        cin >> op;
        if (op == 1) {
            cin >> l >> r >> x;
            insert(l, r, x);
        } else {
            cin >> i;
            cout << get(i) << endl;
        }
    }
    return 0;
}