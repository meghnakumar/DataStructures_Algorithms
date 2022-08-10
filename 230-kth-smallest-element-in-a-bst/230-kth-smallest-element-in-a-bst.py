# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        array=[]
        tree = self.buildArray(root,array)
        tree.sort()
        print(tree)
        for i in range(len(tree)):
            print i,k-1
            if i==k-1:
                return tree[i]
        return 0
        
    def buildArray(self,root,array):
        if root is not None:
            array.append(root.val)
            self.buildArray(root.left,array) and self.buildArray(root.right,array)
        return array