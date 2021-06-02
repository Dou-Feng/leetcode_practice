#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

class Solution {
public:
    int magicTower(vector<int>& nums) {
        int t = 0;
        long long hp = 1;
        priority_queue<ll, vector<ll>, greater<ll>> pq;
        vector<ll> back;
        for (auto &e : nums) {
            if (e >= 0) {
                hp += e;
            } else {
                pq.push(e);
                hp += e;
                while (!pq.empty() && hp <= 0) {
                    hp -= pq.top();
                    back.emplace_back(pq.top());
                    t++;
                    pq.pop();
                }
            }
        }
        // cout << hp << endl;
        for (auto &e : back) {
            hp += e;
            if (hp <= 0) return -1;
        }
        return t;
    }
};

int main() {
    Solution sol;
    vector<int> input({100,100,100,-250,-60,-140,-50,-50,100,150});
    cout << sol.magicTower(input) << endl;
    return 0;
}