from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        que = []
        max_cnt, base, num = 0, 10**9+7, 0
        ans = []
        if root:
            que.append(root)
        while que:
            p = que[-1]
            while p.left:
                que.append(p.left)
                p = p.left
            print(p.val)
            p = que.pop()
            if base == p.val:
                num += 1
            else:
                base = p.val
                num = 1
                
            if num > max_cnt:
                max_cnt = num
                ans = [p.val]
            elif num == max_cnt:
                ans.append(p.val)
            
            if p.right:
                que.append(p.right)

        return ans
            

sol = Solution()
root = TreeNode(1)
root.left = TreeNode(1)
root.right = TreeNode(2)
s = sol.findMode(root)
        
            
            
            
                