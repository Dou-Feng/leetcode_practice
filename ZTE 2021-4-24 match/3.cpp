#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <unordered_map>
#include <queue>
#include <unordered_set>
#include <stack>

using namespace std;


int n;
int level;
int type;
int main() {
    type = 0;
    vector<stack<int>> tasks(5);
    cin >> n;
    for (int i = 1; i <= n; ++i) {
        cin >> level;
        level--;
        if (tasks[level].size() == 0) {
            type++;
        }
        tasks[level].push(i);
        if (type == 5) {
            for (int j = 0; j < 5; ++j) {
                cout << tasks[j].top() << " ";
                tasks[j].pop();
                if (tasks[j].size() == 0) --type;
            }
            cout << endl;
        } else {
            cout << "-1" << endl;
        }
    }

    return 0;
}