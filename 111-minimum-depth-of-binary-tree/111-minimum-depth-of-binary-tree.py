# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root,depth=0):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return depth
        depth=depth+1
        if root.left is not None and root.right is not None:
            return min(self.minDepth(root.left, depth), self.minDepth(root.right, depth))
        if root.left is None and root.right is not None:
            return self.minDepth(root.right,depth)
        else:
            return self.minDepth(root.left,depth)
        return depth
        