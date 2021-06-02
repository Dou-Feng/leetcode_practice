#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <unordered_map>
#include <queue>
#include <unordered_set>
#include <numeric>

using namespace std;

int n1, n2, q;
vector<int> loc(200005);
vector<int> type(200005);

int main() {
    cin >> n1 >> n2 >> q;
    iota(loc.begin() + 1, loc.begin() + 1 + n1, 1);
    iota(loc.begin() + n1 + 1, loc.begin()+1+n1+n2, 1);
    for (int i = 1; i <= n1; ++i) {
        type[i] = 1;
    }
    for (int i = n1+1; i <= n1+n2; ++i) {
        type[i] = 2;
    }
    int last1 = n1 + 1, last2 = n2 + 1;
    int t;
    for (int i = 0; i < q; ++i) {
        cin >> t;
        if (type[t] == 1) {
            type[t] = 2;
            loc[t] = last2++;
        } else {
            type[t] = 1;
            loc[t] = last1++;
        }
    }
    vector<pair<int,int>> r1, r2;
    for (int i = 1; i <= n1+n2; ++i) {
        if (type[i] == 1) {
            r1.push_back({loc[i], i});
        } else {
            r2.push_back({loc[i], i});
        }
    }
    sort(r1.begin(), r1.end());
    sort(r2.begin(), r2.end());
    for (auto e : r1) {
        cout << e.second << " ";
    }
    cout << endl;
    for (auto e : r2) {
        cout << e.second << " ";
    }
    cout << endl;
    return 0;
}