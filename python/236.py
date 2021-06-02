from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # if the node left child contain one of the p,q, then the node is the ans
        # if not root:
        #     return None
        # if not root.left and not root.right:
        #     return root
        def traverse(root, t):
            # print("hello")
            if not root:
                return []
            if root == t:
                return [root]
            path1 = traverse(root.left, t)
            path2 = traverse(root.right, t)
            if path1:
                return path1 + [root]
            elif path2:
                return path2 + [root]
            else:
                return []
        
        path1 = traverse(root, p)[::-1]
        path2 = traverse(root, q)[::-1]
        print(path1)
        i = 0
        while i < len(path1) and i < len(path2) and path1[i] == path2[i]:
                i += 1
            
        return path1[i-1]

if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(1)
    s = sol.lowestCommonAncestor(root, 1, 1)
    print(s)