# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        res = 0
        stack = [(root,0)]

        while stack:
            node, total = stack.pop()

            total = (total<<1) | node.val
            if node.left is None and node.right is None:
                res += total
            else:
                if node.right:
                    stack.append((node.right, total))
                if node.left:
                    stack.append((node.left, total))
        
        return res