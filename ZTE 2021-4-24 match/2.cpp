#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <unordered_map>
#include <queue>
#include <unordered_set>

using namespace std;


int T;
long long l;

long long solve(long long l) {
    if (l == 1) return 1;
    if (l % 2) {
        return solve(l / 2 + 1) + 1;
    } else {
        return solve(l / 2) + 1;
    }
}

int main() {
    cin >> T;
    while (T--) {
        cin >> l;
        cout << solve(l) << endl;
    }
    
    return 0;
}