# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = [p, q]
        while len(queue) > 0:
            pop1 = queue.pop(0)
            pop2 = queue.pop(0)
            if (pop1 == None) ^ (pop2 == None):
                return False
            if pop1 == None and pop2 == None:
                continue
            if (pop2.val != pop1.val):
                return False
            queue.append(pop1.left)
            queue.append(pop2.left)
            queue.append(pop1.right)
            queue.append(pop2.right)
        return True