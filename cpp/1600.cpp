#include <bits/stdc++.h>
#include<unordered_set>
#include<unordered_map>
using namespace std;

struct Node {
    Node(string name) : name(name) {
        left = nullptr;
        right = nullptr;
    }
    Node* left, *right;
    string name;
};

class ThroneInheritance {
    unordered_map<string, Node*> loc;
    unordered_set<string> dead;
    Node* root;
public:
    ThroneInheritance(string kingName) {
        root = new Node(kingName);
        loc[kingName] = root;
    }
    
    void birth(string parentName, string childName) {
        Node *p = loc[parentName];
        if (!p->left) {
            p->left = new Node(childName);
            loc[childName] = p->left;
        } else {
            p = p->left;
            while (p->right) {
                p = p->right;
            }
            p->right = new Node(childName);
            loc[childName] = p->right;
        }
    }
    
    void death(string name) {
        dead.insert(name);
    }
    
    void preOrder(Node *root, vector<string> &ans) {
        if (!root) return;
        if (dead.find(root->name) != dead.end())
            ans.push_back(root->name);
        preOrder(root->left, ans);
        preOrder(root->right, ans);
    }

    vector<string> getInheritanceOrder() {
        vector<string> ans;
        preOrder(root, ans);
        return ans;
    }
};

/**
 * Your ThroneInheritance object will be instantiated and called as such:
 * ThroneInheritance* obj = new ThroneInheritance(kingName);
 * obj->birth(parentName,childName);
 * obj->death(name);
 * vector<string> param_3 = obj->getInheritanceOrder();
 */

int main() {
    ThroneInheritance* obj = new ThroneInheritance("king");
    obj->birth("king","Alice");
    obj->birth("king","Bob");
    obj->birth("Alice","Jack");
    // obj->death(name);
    vector<string> s = obj->getInheritanceOrder();
    for (auto e : s) {
        cout << e << endl;
    }
    return 0;
}