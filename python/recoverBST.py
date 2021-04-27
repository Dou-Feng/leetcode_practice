
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        pre = None
        front, back = None, None

        stack = [root]
        p = stack[0]
        while p.left:
            stack.append(p.left)
            p = p.left

        while len(stack) > 0:
            node = stack.pop()
            if not front and pre and pre.val > node.val:
                front = pre
            if pre and pre.val > node.val:
                back = node
            pre = node
            if node.right:
                stack.append(node.right)
                p = node.right
                while p.left:
                    stack.append(node.left)
                    p = p.left


        if not front or not back:
            return
        # swap two nodes
        temp = front.val
        front.val = back.val
        back.val = temp

        
sol = Solution()
tree = TreeNode(6)
tree.left = TreeNode(1)
sol.recoverTree(tree)
        
