# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def check(self, node):
        if node == None:
            return 0
        return max(self.check(node.left), self.check(node.right)) + 1

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.check(root)