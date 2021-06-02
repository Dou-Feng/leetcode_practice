# Definition for a binary tree node.
from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq
import copy


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        # bfs
        que = []
        if root:
            que.append(root)

        i = 0
        ret = 0
        while i < len(que):
            l = len(que)
            sum = 0
            for j in range(i, l):
                sum += que[j].val
                if que[j].left:
                    que.append(que[j].left)
                if que[j].right:
                    que.append(que[j].right)

            ret = sum
            i = l

        return ret




if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.left.left = TreeNode(2)
    s = sol.deepestLeavesSum(root)
    print(s)
