# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root, depth=0):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth=depth+1
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return depth
        return max(self.maxDepth(root.left, depth), self.maxDepth(root.right, depth))
        