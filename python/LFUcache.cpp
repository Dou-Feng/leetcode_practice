#include <bits/stdc++.h>
#include <unordered_map>

using namespace std;

class Node {
public:
    int frequent, time, key, value;

    Node(int _frequent, int _time, int _key, int _value) : frequent(_frequent), time(_time), key(_key), value(_value) {}

    bool operator<(const Node &n) const {
        return this->frequent < n.frequent || (this->frequent == n.frequent and this->time < n.time);
    }

};


class LFUCache {
public:
    int capacity;
    unordered_map<int, Node> dict;
    set<Node> lfu;
    int time;

    LFUCache(int capacity) {
        this->capacity = capacity;
        time = 0;
        dict.clear();
        lfu.clear();
    }
    
    int get(int key) {
        // for (auto it : dict) {
        //     cout << it.first << ", " << it.second.value << endl;
        // }
        if (dict.find(key) != dict.end()) {
            auto it = dict.find(key);
            
            lfu.erase(it->second);
            it->second.frequent += 1;
            it->second.time = ++time;
            lfu.insert(it->second);
            
            return it->second.value;
        }
        return -1;
    }
    
    void put(int key, int value) {
        auto it = dict.find(key);
        if (dict.size() == capacity && it == dict.end()) {
            // eliminate 
            auto p = lfu.begin();
            dict.erase(p->key);
            lfu.erase(p);
        }
        if (it != dict.end()) {
            lfu.erase(it->second);
            it->second.value = value;
            it->second.frequent += 1;
            it->second.time = ++time;
            lfu.insert(it->second);
        } else {
            // add a new node
            Node p = Node(1, ++time, key, value);
            dict.insert(make_pair(key, p));
            lfu.insert(p);
            // cout << "add a new node" << endl;
            
        }
    }
};

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache* obj = new LFUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */

// ["LFUCache","put","put","get","put","get","get","put","get","get","get"]
// [[2],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]
int main() {
    LFUCache cache(2);
    cache.put(1, 1);
    cache.put(2, 2);
    cout << cache.get(1) << ", ";
    cache.put(3, 3);
    cout << cache.get(2) << ", ";
    cout << cache.get(3) << ", ";
    cache.put(4, 4);
    cout << cache.get(1) << ", ";
    cout << cache.get(3) << ", ";
    cout << cache.get(4) << endl;


    return 0;
}