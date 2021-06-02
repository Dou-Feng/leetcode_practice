#include <bits/stdc++.h>

using namespace std;
// #define debug

class MKAverage {
public:
    int m, k;
    queue<int> container;
    multiset<int> small, big, middle;
    long long msum = 0;
    void shiftleft(multiset<int>&l, multiset<int>& r) {
        l.insert(*r.begin());
        r.erase(r.begin());
    }
    void shiftright(multiset<int>& l, multiset<int>& r) {
        r.insert(*l.rbegin());
        l.erase(--l.end());
    }

    
    MKAverage(int m, int k) {
        this->m = m, this->k = k;
    }
    
    void addElement(int num) {
        container.push(num);
        
        if (small.size() && *small.rbegin() >= num) {
            small.insert(num);
        } else if (big.size() && *big.begin() <= num) {
            big.insert(num);
        } else {
            msum += num;
            middle.insert(num);
        }
        
        while (small.size() > k) { msum += *small.rbegin(); shiftright(small, middle); }
        while (big.size() > k) { msum += *big.begin(); shiftleft(middle, big); }

        // 如果 container 的元素数量大于 m
        if (container.size() > m) {
            int front = container.front(); container.pop();
            if (small.find(front) != small.end()) small.erase(small.find(front));
            else if (middle.find(front) != middle.end()) { middle.erase(middle.find(front)); msum -= front; }
            else big.erase(big.find(front));
        }
        
        if (container.size() >= m) {
            while (small.size() < k) { msum -= *middle.begin() ;shiftleft(small, middle); }
            while (big.size() < k) { msum -= *middle.rbegin(); shiftright(middle, big); }
        }

    }
    
    int calculateMKAverage() {
        if (container.size() < m) return -1;
        return msum / (m - 2 *k);
    }
};
    
    /**
     * Your MKAverage object will be instantiated and called as such:
     * MKAverage* obj = new MKAverage(m, k);
     * obj->addElement(num);
     * int param_2 = obj->calculateMKAverage();
     */

    int main() {
        MKAverage obj(3, 1); 
        obj.addElement(3);        // 当前元素为 [3]
        obj.addElement(1);        // 当前元素为 [3,1]
        cout << obj.calculateMKAverage() << endl; // 返回 -1 ，因为 m = 3 ，但数据流中只有 2 个元素
        obj.addElement(10);       // 当前元素为 [3,1,10]
        cout << obj.calculateMKAverage() << endl; // 最后 3 个元素为 [3,1,10]
                                // 删除最小以及最大的 1 个元素后，容器为 [3]
                                // [3] 的平均值等于 3/1 = 3 ，故返回 3
        obj.addElement(5);        // 当前元素为 [3,1,10,5]
        obj.addElement(5);        // 当前元素为 [3,1,10,5,5]
        obj.addElement(5);        // 当前元素为 [3,1,10,5,5,5]
        cout << obj.calculateMKAverage() << endl; // 最后 3 个元素为 [5,5,5]
                                // 删除最小以及最大的 1 个元素后，容器为 [5]
                                // [5] 的平均值等于 5/1 = 5 ，故返回 5
        
    }