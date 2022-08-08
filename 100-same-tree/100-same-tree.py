# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is not None and q is not None:
            if p.val == q.val:
                # if p.left is None or q.left is None:
                #     return False
                # if p.right is None or q.right is None:
                #     return False
                # if p.left is not None and q.left is not None:
                #     return self.isSameTree(p.left,q.left)
                # if p.right is not None and q.right is not None:
                #     return self.isSameTree(p.right,q.right)
                return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        else:
            return p==q
    