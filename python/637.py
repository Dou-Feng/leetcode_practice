from typing import List
import queue
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        que = queue.deque()
        
        if root:
            que.append(root)

        ret = []
        while que:
            new_que = queue.deque()
            s = 0
            n = 0
            while que:
                top = que.popleft()
                s += top.val
                n += 1
                if top.left:
                    new_que.append(top.left)
                if top.right:
                    new_que.append(top.right)

            ret.append(s / n)

            que = new_que
        return ret





if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(sol.averageOfLevels(root))