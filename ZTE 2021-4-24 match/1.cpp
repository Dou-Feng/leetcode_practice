#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <unordered_map>
#include <queue>
#include <unordered_set>

using namespace std;


int n, h, u;

int a[500005];

int main() {
    cin >> n >> h >> u;
    int ans = 0;
    int last = u - h;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }
    sort(a, a+n);
    int i = n-1;
    while (last > 0) {
        last -= a[i--];
        ++ans;
    }
    cout << ans << endl;
    return 0;
}