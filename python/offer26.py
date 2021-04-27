# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def subTree(A, B):
            if not A and not B:
                return True
            elif not A or not B or A.val != B.val:
                return False

            left = (not B.left) or subTree(A.left, B.left)
            right = (not B.right) or subTree(A.right, B.right)
            # print(A.val, B.val, left, right)
            return left and right

        def dfs(A):
            if subTree(A, B):
                return True
            if A.left and dfs(A.left):
                return True
            if A.right and dfs(A.right):
                return True

            return False

        return dfs(A) if A else False

sol = Solution()
A = TreeNode(1)
A.left = TreeNode(0)
A.right = TreeNode(1)
A.left.left = TreeNode(-4)
A.left.right = TreeNode(-3)

B = TreeNode(1)
B.left = TreeNode(-4)
print(sol.isSubStructure(A, B))

A = TreeNode(4)
A.left = TreeNode(2)
A.right = TreeNode(3)
A.left.left = TreeNode(4)
A.left.right = TreeNode(5)
A.right.left = TreeNode(6)
A.right.right = TreeNode(7)
A.left.left.left = TreeNode(8)
A.left.left.right = TreeNode(9)

B = TreeNode(4)
B.left = TreeNode(8)
B.right = TreeNode(9)
print(sol.isSubStructure(A, B))