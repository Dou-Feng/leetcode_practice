#include <bits/stdc++.h>

using namespace std;

int n;
long long y;
pair<int, bool> scores[100005];


int main() {
    cin >> n;
    int right = 0;
    for (int i = 0; i < n; ++i) {
        cin >> scores[i].first >> scores[i].second;
        if (scores[i].second) {
            right++;
        }
    }
    sort(scores, scores+n);
    int max_right = right;
    int ret  = scores[0].first;
    int i = 0, j = 0;
    while (j < n) {
        while (j < n && scores[i].first == scores[j].first) {
            if (scores[j].second) {
                right--;
            } else {
                right++;
            }
            j++;
        }
        if (right >= max_right) {
            max_right = right;
            ret = scores[j].first;
        }
        i = j;
    }
    cout << ret << endl;
    return 0;
}