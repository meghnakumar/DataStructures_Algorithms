# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.checkSym(root.left,root.right)
           
        
    def checkSym(self,p,q):
        if p is not None and q is not None:
            if p.val == q.val:
                return self.checkSym(p.left,q.right) and self.checkSym(p.right,q.left)
        
        else:
            return p==q
        
        