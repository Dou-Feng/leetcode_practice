// #include <bits/stdc++.h>
#include <string>
#include <iostream>

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

bool validPath(string path) {
    if (path.size() <= 1) {return false;}
    path = path.substr(1);
    int j;
    while ((j = path.find('/')) != path.size()) {
        string sub = path.substr(0, j);
        if (sub.size() == 0) return false;
        for (auto c : sub) {
            if ((c<'0' && c >'9') || (c < 'a' && c >'z') || (c <'A' && c>'Z')) return false;
        }
        path = path.substr(j);
    }
    return true;
}
bool createNormalFile(string fileapth, ll size) {
    if(!validPath(fileapth)) {return false;}
    TreeNode *parent = root, *p, *q;
    int i = 1, j;
    int n = fileapth.size();
    string sub;
    while (i < n) {
        j = i + 1;
        while (j < n && fileapth[j] != '/') ++j;
        sub = fileapth.substr(i, j - i);
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
            } else {
                // 如果q不存在，那么需要创建一个新的目录
                if (p == parent) {
                    p->child = new TreeNode(sub);
                    parent = p->child;
                } else {
                    p->sibling = new TreeNode(sub);
                    parent = p->sibling;
                }
            }
        } else {
            // 如果是最后一跳
            if (q) {
                if (q->type == 1) {return false;}
                q->cd = size;
            } else {
                // 如果q不存在，那么需要创建一个新的普通文件
                if (p == parent) {
                    p->child = new TreeNode(sub);
                    p->child->cd = size;
                    p->child->type = 0;
                    parent = p->child;
                } else {
                    p->sibling = new TreeNode(sub);
                    p->child->cd = size;
                    p->child->type = 0;
                    parent = p->sibling;
                }
            }
        }

        i = j+1;
    }
    return true;
}

bool removeFile(string filename) {
    
    return true;
}

bool setSize(string filepath, ll ld, ll lr)  {
    return true;
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
    }
    return 0;
}