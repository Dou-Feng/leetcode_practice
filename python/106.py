from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
        def mbuildTree(l, r, last):
            if last < 0:
                return None
            
            if l + 1 == r:
                return TreeNode(postorder[last])

            mid = inorder[l:r].index(postorder[last]) + l

            root = TreeNode(postorder[last])
            last -= 1
            if last < 0:
                return root
            left_last, right_last = last, last
            while left_last >= 0 and postorder[left_last] not in inorder[l:mid]:
                left_last -= 1

            while right_last >= 0 and postorder[right_last] not in inorder[mid+1:r]:
                right_last -= 1
            print("l, r, mid, last, left_last, right_last")
            print(l, r, mid, last, left_last, right_last)
            root.left = mbuildTree(l, mid, left_last)
            root.right = mbuildTree(mid+1, r, right_last)

            return root

        return mbuildTree(0, len(inorder), len(postorder)-1)

def TreeTraverse(root):
    if not root:
        return
    print(root.val)
    TreeTraverse(root.left)
    TreeTraverse(root.right)

sol = Solution()
s = sol.buildTree([9,3,15,20,7], [9,15,7,20,3])
TreeTraverse(s)