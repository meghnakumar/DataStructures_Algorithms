# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True
        leftH=self.checkHiegth(root.left)
        print(leftH)
        rightH = self.checkHiegth(root.right)
        print(rightH)
        if abs(leftH-rightH) >1:
            print("Value greater")
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
            # return self.isBalanced(root.right)
        return True
        
    
    def checkHiegth(self,branch,depth=0):
        if branch is None:
            return depth
        depth=depth+1
        if branch.left is None and branch.right is None:
            return depth
        return max(self.checkHiegth(branch.left, depth), self.checkHiegth(branch.right, depth))
        