# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = [root]
        while len(queue) > 0:
            item = queue.pop(0)
            if item == None:
                continue
            item.right, item.left = item.left, item.right
            queue.append(item.left)
            queue.append(item.right)
        return root