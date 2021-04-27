// #include <bits/stdc++.h>
#include <string>
#include <iostream>
#include <vector>

using namespace std;
typedef long long ll;

struct TreeNode {
    TreeNode() : child(nullptr), sibling(nullptr), type(1), ld(0), lr(0), cd(0), cr(0) {}
    TreeNode(string na) : name(na), child(nullptr), sibling(nullptr), type(1), ld(0), lr(0), cd(0), cr(0)  {}
    TreeNode *child, *sibling;
    string name;
    ll ld, lr;
    ll cd, cr; // 如果是普通文件，那么cd也表示文件大小
    int type; // type == 1 is dir, type == 0 is normal
};

TreeNode* root = new TreeNode("/");

void deleteNodes(TreeNode *pre, vector<TreeNode*> new_create, int type) { // type = 1 说明连接他的是双亲结点，type = 0 说明连接它的是兄弟结点
    if (new_create.empty()) return;
    if (type) {
        pre->child = nullptr;
    } else {
        pre->sibling = nullptr;
    }
    for (auto e : new_create) {
        delete e;
    }
}

bool createNormalFile(string filepath, ll size) {
    TreeNode *parent = root, *p, *q, *pre;
    int type = -1;
    int i = 1, j;
    int n = filepath.size();
    string sub;

    // 初始化一个路径数组，用来保存走过的路径，另外一个数组保存新创建的结点
    vector<TreeNode*> paths, new_create;
    paths.push_back(root);
    while (i < n) {
        j = i + 1;
        while (j < n && filepath[j] != '/') ++j;
        sub = filepath.substr(i, j - i);
        p = parent;
        q = parent->child;
        while (q && q->name != sub) {
            p = q;
            q = q->sibling;
        }
        // 如果 j != n, 说明是目录
        if (j != n) {
            if (q) {
                // 如果 q 存在，那么必须为目录
                if (q->type != 1) {return false;}
                parent = q;
                paths.push_back(parent);
            } else {
                // 如果q不存在，那么需要创建一个新的目录
                if (p == parent) {
                    if (type == -1) {
                        type = 1;
                        pre = p;
                    }
                    p->child = new TreeNode(sub);
                    parent = p->child;
                } else {
                    if (type == -1) {
                        type = 0;
                        pre = p;
                    }
                    p->sibling = new TreeNode(sub);
                    parent = p->sibling;
                }
                
                paths.push_back(parent);
                new_create.push_back(parent);
            }
        } else {
            // 如果是最后一跳
            if (q) {
                if (q->type == 1) {return false;}
                // 暂不修改
                // q->cd = size;
                paths.push_back(q);
            } else {
                // 如果q不存在，那么需要创建一个新的普通文件
                if (p == parent) {
                    if (type == -1) {
                        type = 1;
                        pre = p;
                    }
                    p->child = new TreeNode(sub);
                    p->child->type = 0;
                    parent = p->child;
                } else {
                    if (type == -1) {
                        type = 0;
                        pre = p;
                    }
                    p->sibling = new TreeNode(sub);
                    p->sibling->type = 0;
                    parent = p->sibling;
                }
                paths.push_back(parent);
                new_create.push_back(parent);
            }
        }

        i = j+1;
    }

    if (paths.size() == 1) {
        deleteNodes(pre, new_create, type);
        return false;
    }
    // 需要考虑路径上所有的结点的配额是否满足
    TreeNode *lastnode = paths.back();
    ll diff = size - lastnode->cd;
    for (int i = 0; i < paths.size()-1; ++i) {
        // 所有前置的结点都考虑 lr.
        TreeNode *cur = paths[i];
        if (cur->lr != 0 && cur->lr < cur->cr + diff) {
            deleteNodes(pre, new_create, type);
            return false;
        }
    }
    // 考虑直接双亲结点
    TreeNode *pa = paths[paths.size()-2];
    if (pa->ld != 0 && pa->ld < pa->cd + diff) {
        deleteNodes(pre, new_create, type);
        return false;
    }
    // 对结点进行修改
    for (int i = 0; i < paths.size()-1; ++i) {
        // 所有结点都考虑 lr.
        TreeNode *cur = paths[i];
        cur->cr += diff;
    }
    pa->cd += diff;
    // 最后修改最后一个结点的值
    lastnode->cd += diff;

    return true;
}

void printTree(TreeNode* root) {
    if (!root) return;
    cout << root->name << ", " << root->cd << "/" << root->ld << " ; " << root->cr << "/" << root->lr << endl;
    printTree(root->child);
    printTree(root->sibling);
}

void destroy(TreeNode *root) {
    if (!root) return;
    destroy(root->child);
    destroy(root->sibling);
    delete root;
}

bool removeFile(string filename) {
    TreeNode *parent = root, *p, *q;
    int i = 1, j;
    int n = filename.size();
    string sub;

    // 初始化一个路径数组，用来保存走过的路径
    vector<TreeNode*> paths;
    TreeNode* pre;
    paths.push_back(root);
    while (i < n) {
        j = i + 1;
        while (j < n && filename[j] != '/') ++j;
        sub = filename.substr(i, j - i);
        p = parent;
        q = parent->child;
        while (q && q->name != sub) {
            p = q;
            q = q->sibling;
        }
        if (!q) {
            return true;
        }
        if (j == n) {
            pre = p;
        }
        paths.push_back(q);
        parent = q;
        i = j+1;
    }
    // 假设不存在删除根结点这么蠢的行为
    ll cd = paths.back()->cd, cr = paths.back()->cr;
    
    // destroy child
    destroy(paths.back()->child);
    parent = paths[paths.size()-2];
    if (pre != parent) {
        pre->sibling = paths.back()->sibling;
    } else {
        pre->child = paths.back()->sibling;
    }
    // 如果是一个普通文件，那么修改parent结点的cd
    if (paths.back()->type == 0) {
        parent->cd -= cd;
    }
    // 修改cr
    for (int i = 0; i < paths.size()-1; ++i) { 
        paths[i]->cr -= max(cd, cr);
    }
    // 最后删除该结点
    delete paths.back();
    return true;
}

bool setSize(string filepath, ll ld, ll lr)  {
    TreeNode *parent = root, *p, *q = root;
    int i = 1, j;
    int n = filepath.size();
    string sub;

    while (i < n) {
        j = i + 1;
        while (j < n && filepath[j] != '/') ++j;
        sub = filepath.substr(i, j - i);
        p = parent;
        q = parent->child;
        while (q && q->name != sub) {
            p = q;
            q = q->sibling;
        }
        if (!q || q->type == 0) return false;
        parent = q;
        i = j+1;
    }

    if ((q->cd <= ld || ld == 0) && (lr == 0 || q->cr <= lr)) {
        q->ld = ld;
        q->lr = lr;
        return true;
    } else {
        return false;
    }
}

int main() {
    int op;
    cin >> op;
    string filepath;
    ll size, ld, lr;
    char a;
    bool ans;
    while (op--) {
        cin >> a;
        switch (a)
        {
        case 'C':
            cin >> filepath >> size;
            ans = createNormalFile(filepath, size);
            break;
        case 'R':
            cin >> filepath;
            ans = removeFile(filepath);
            break;
        case 'Q':
            cin >> filepath >> ld >> lr;
            ans = setSize(filepath, ld, lr);
            break;
        }
        cout << (ans ? "Y" : "N") << endl;
        // cout << "Debug::" << "Tree pre traverse" << endl;
        // printTree(root); cout << endl << endl;
    }
    return 0;
}