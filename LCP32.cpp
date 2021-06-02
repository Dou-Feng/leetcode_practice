#include <bits/stdc++.h>

using namespace std;

using PII=pair<int, int>;

class Solution {
public:
    vector<int> times;
    void getAllTimes(vector<vector<int>>& tasks) {
        for (int i = 0; i < tasks.size(); i++) {
            times.push_back(tasks[i][0]);
            times.push_back(tasks[i][1]+1);
        }
        sort(times.begin(), times.end());
        times.resize(unique(times.begin(), times.end()) - times.begin());

    }
    int processTasks(vector<vector<int>>& tasks) {
        getAllTimes(tasks);
        sort(tasks.begin(), tasks.end());
        priority_queue<PII, vector<PII>, greater<PII>> pq;
        int ans = 0, extra = 0, cur = 0;
        for (int i = 0; i < times.size() - 1; ++i) {
            int curtime = times[i];
            int seg = times[i+1] - times[i];
            while (!pq.empty() && pq.top().second < curtime) {
                pq.pop();
            }
            while (cur < tasks.size() && tasks[cur][0] == curtime) {
                pq.push({extra + tasks[cur][1] - curtime + 1 - tasks[cur][2], tasks[cur][1]});
                cur++;
            }

            if (!pq.empty()) {
                int min_seg = pq.top().first - extra;
                if (min_seg < seg) {
                    ans += seg - min_seg;
                    seg = min_seg;
                }
            }
            extra += seg;
        }
        return ans;
    }
};


