import math
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
       
        # if there are many N branches, there return value is list containing N elements.
        def branch_sum(root):
            if not root:
                return []
            elif not root.left and not root.right:
                return [str(root.val)]
            else:
                sub_branch = branch_sum(root.left)
                sub_branch += branch_sum(root.right)
                print(sub_branch)
                ret = []
                for e in sub_branch:
                    ret.append(str(root.val) + e)
                
                return ret
        str_res = branch_sum(root)
        ans = 0
        for s in str_res:
            ans += int(s)
        return ans


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    root.left.left = TreeNode(7)
    root.left.right = TreeNode(0)
    root.left.right.left = TreeNode(0)

    root.right.left = TreeNode(6)
    print(sol.sumNumbers(root))