# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if root is None:
            return False
        if subRoot is None:
            return True
        if self.checkSub(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        
    
    
    def checkSub(self,root,subRoot):
        if root is None and subRoot is None:
            return True
        if root is not None and subRoot is not None and  root.val==subRoot.val:
            return self.checkSub(root.left,subRoot.left) and self.checkSub(root.right,subRoot.right)
        return False
        
        
        