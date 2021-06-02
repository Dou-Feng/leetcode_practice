#include <bits/stdc++.h>

using namespace std;

const static int MAXL = 16;

class SkiplistNode {
public:
    // 相当于个多层链表的 next 结点
    // this->level[i] 表示所处为 i 层的当前结点的下一个结点
    vector<SkiplistNode*> level;
    // 当然我们需要记录当前结点的值
    int val;
    SkiplistNode(int v = INT_MAX, int sz = MAXL) : val(v), level(sz, nullptr) {};
};

class Skiplist {
public:
    // 记录当前的跳表元素个数
    int length = 0;
    // 记录当前跳表的最大层数
    int level = 1;
    const int S = 0xffff;
    const int PS = S / 4;

    // 记录头部信息
    SkiplistNode *head, *tail;

    Skiplist() {
        srand(time(NULL));
        head = new SkiplistNode(0);
        tail = new SkiplistNode(INT_MAX, 0);
        // 添加边界，最左端为 head，最右端为 tail
        for (int i = 0; i < MAXL; ++i) {
            head->level[i] = tail;
        }
    }
    
    int randomLevel() {
        int lv = 1;
        // MAXL = 32, S = 0xFFFF, PS = S * P, P = 1 / 4
        while ((rand() & S) < PS) ++lv;
        return min(MAXL, lv);
    }

    SkiplistNode* find(int target) {
        SkiplistNode* p = head;
        for (int i = level - 1; i >= 0; --i) {
            while (p->level[i] && p->level[i]->val < target) {
                p = p->level[i];
            }
        }
        p = p->level[0];
        return p;
    }

    bool search(int target) {
        SkiplistNode* p = find(target);
        return p->val == target;
    }
    
    void add(int num) {
        vector<SkiplistNode*> update(MAXL, head);
        SkiplistNode *p = head;
        for (int i = level - 1; i >= 0; --i) {
            while (p->level[i] && p->level[i]->val < num) {
                p = p->level[i];
            }
            update[i] = p;
        }
        // 如果不允许重复元素，直接返回
        /* 
        p = p->level[0];
        if (p->val == num) {
            return ;
        }
        */
       // 首先，随机一下新添加的结点有多少层
       int ranl = randomLevel();
       // 防止 level 跳级增长
       if (ranl > level) {
           ranl = ++level;
       }
       SkiplistNode *newnode = new SkiplistNode(num);
       ++length;
       // 逐层修改跳表
       for (int i = 0; i < ranl; ++i) {
            newnode->level[i] = update[i]->level[i];
            update[i]->level[i] = newnode;
       }
    }
    
    bool erase(int num) {
        vector<SkiplistNode*> update(MAXL, head);
        SkiplistNode *p = head;
        for (int i = level - 1; i >= 0; --i) {
            while (p->level[i] && p->level[i]->val < num) {
                p = p->level[i];
            }
            update[i] = p;
        }
        p = p->level[0];
        // 如果不存在该元素
        if (p->val != num) {
            return false;
        }
        for (int i = 0; i < level; ++i) {
            if (update[i]->level[i] != p) break;
            update[i]->level[i] = p->level[i];
        }
        delete p;
        --length;
        // 修改 level, level 最小值为 1，要保证不能低于 1
        if (level > 1 && head->level[level-1] == tail) --level;
        return true;
    }
};

/**
 * Your Skiplist object will be instantiated and called as such:
 * Skiplist* obj = new Skiplist();
 * bool param_1 = obj->search(target);
 * obj->add(num);
 * bool param_3 = obj->erase(num);
 */

int main() {
    Skiplist* obj = new Skiplist();
    srand(time(NULL));
    vector<int> gt;
    for (int i = 0; i < 10; ++i) {
        int e = rand() % 100;
        obj->add(e);
        gt.emplace_back(e);
    }
    cout << "Test Start!!" << endl;
    // test 1
    int test_case = 10000;
    while (test_case--) {
        int op = rand() % 3;
        int i, e;
        switch (op) {
            case 0: // add
            e = rand() % RAND_MAX;
            cout << "add " << e << "; ";
            obj->add(e);
            gt.emplace_back(e);
            break;
            case 1: // find
            if (gt.empty()) continue;
            e = rand() % gt.size();
            cout << "find " << e << "; ";
            if (!obj->find(gt[e])) {
                cout << "Can't find " << e << endl;
                return 0;
            }
            break;
            case 2: // erase
            if (gt.empty()) continue;
            i = rand() % gt.size();
            e = gt[i];
            gt.erase(gt.begin() + i);
            cout << "erase " << e << "; ";
            if (!obj->erase(e)) {
                cout << "Erase failed, the element = " << e << endl;
                return 0;
            }
            break;
        }
        if (test_case % 20 == 0) cout << endl;
    }
    cout << "Pass!" << endl;
    return 0;
}