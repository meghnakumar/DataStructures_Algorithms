# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        array=[]
        if root is None:
            return root
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left,root.right = root.right,root.left
        return root
        
           
        
    # def checkSym(self,p,q):
    #     if p is not None and q is not None:
    #         p.val=q.val
    #         return self.checkSym(p.left,q.right) and self.checkSym(p.right,q.left)
    #     return p
    
    