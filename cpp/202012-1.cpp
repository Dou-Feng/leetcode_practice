#include <bits/stdc++.h>

using namespace std;

int n;
long long y;

int main() {
    cin >> n;
    long long score, w;
    while (n--) {
        cin >> w >> score;
        y += w * score;
    }
    cout << (y > 0 ? y : 0) << endl;
    return 0;
}