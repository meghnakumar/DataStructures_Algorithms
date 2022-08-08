# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum, calcSum = 0):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if root is None:
            return False
        calcSum = calcSum + root.val
        if not root.left and not root.right and calcSum==targetSum:
            return True
        # if root.left and root.right is not None:
        #     isLeaf = False
        return self.hasPathSum(root.left, targetSum, calcSum) or self.hasPathSum(root.right, targetSum, calcSum)