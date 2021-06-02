#include <bits/stdc++.h>

using namespace std;


struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};


class Solution {
public:
    int k;
    void dfs(TreeNode* cur, vector<int>& render) 
    {
        if (cur == NULL) {
            return;
        }
        vector<int> lren(k+2, 0), rren(k+2, 0);
        if (cur->left)
            dfs(cur->left, lren);
        if (cur->right)
            dfs(cur->right, rren);
        
        for (int i = 0; i <= k; ++i) {
            for (int j = 0; j <= k; ++j) {
                render[0] = max(render[0], lren[i] + rren[j]);
                if (i + j + 1 <= k) {
                    render[i+j+1] = max(render[i+j+1], lren[i] + rren[j] + cur->val);
                }
            }
        }   
    }
    int maxValue(TreeNode* root, int k) {
        if (!root) return 0;
        this->k = k;
        vector<int> render(k+2, 0);
        // cout << root->val << ", " << k << endl;
        dfs(root, render);
        int ret = 0;
        for (int i = 0; i <= k; ++i) {
            ret = max(ret, render[i]);
        }
        return ret;
    }
};

void tra(TreeNode* cur) {
    if (!cur) return ;
    cout << cur->val << ", ";
    tra(cur->left);
    tra(cur->right);
}

int main() {
    TreeNode* root = new TreeNode(5);
    root->left = new TreeNode(2);
    root->left->left = new TreeNode(4);
    root->right = new TreeNode(3);
    Solution sol;
    tra(root);
    cout << endl;
    cout << sol.maxValue(root, 2) << endl;
    return 0;
}