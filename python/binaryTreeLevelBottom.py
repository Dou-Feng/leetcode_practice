from typing import List
import queue
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        que = queue.deque()
        if not root:
            return []
        que.append((root, 1))
        last_layer = 1
        layer_res = []
        ret = []
        while que:
            top, layer = que.popleft()
            if top.left:
                que.append((top.left, layer+1))
                # print((top.left.val, layer+1))
            if top.right:
                que.append((top.right, layer+1))
            if layer == last_layer:
                layer_res.append(top.val)
            else:
                last_layer = layer
                ret = [layer_res] + ret
                layer_res = [top.val]

        if layer_res:
            ret = [layer_res] + ret
        
        return ret

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)

sol = Solution()
print(sol.levelOrderBottom(root))

