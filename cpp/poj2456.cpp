#include <iostream>
#include <algorithm>

using namespace std;

typedef long long ll;
int N, C;
ll loc[1000007];


bool check(ll x) {
    int last = C-1;
    ll lloc = loc[0];
    int i = 1;
    while (i < N && last) {
        if (loc[i] - lloc >= x) {
            lloc = loc[i];
            --last;
        }
        ++i;
    }
    return last == 0;
}


int main() {
    cin >> N >> C;
    for (int i = 0; i < N; ++i) {
        cin >> loc[i];
    }
    sort(loc, loc + N);
    
    ll left = 0, right = loc[N-1] - loc[0], mid;
    ll ret;
    while (left <= right) {
        mid = left + (right - left) / 2;
        if (check(mid)) {
            ret = mid;
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    cout << ret << endl;
    // return ret;
    return 0;
}