from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        ans = []
        tmp = []
        def dfs(root, accum):
            if not root:
                return
            if not root.left and not root.right:
                if accum + root.val == sum:
                    tmp.append(root.val)
                    ans.append(tmp.copy())
                    tmp.pop()
                else:
                    return
            
            tmp.append(root.val)
            dfs(root.left, accum+root.val)
            dfs(root.right, accum+root.val)
            tmp.pop()
        
        dfs(root, 0)
        return ans


sol = Solution()
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)
s = sol.pathSum(root, 22)
print(s)