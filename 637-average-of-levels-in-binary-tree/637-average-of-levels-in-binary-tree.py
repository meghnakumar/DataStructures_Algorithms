# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return []
        current=[root]
        result=[]
        
        while current:
            level=[]
            next_level=[]
            
            for node in current:
                level.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            result.append(sum(level)/len(level))
            current=next_level
        return result
        
#         avg=[]
        
#         if root is not None:
#             avg.append(root.val)
#             avg=self.calc(root.left,root.right,avg)
#         return avg
    
#     def calc(lval,rval,avg):
#         if lval and rval is None:
#             return avg
#         avg.append()
#         return (self.calc(val.left)+self.calc(val.right))/2

            
    
        
        
        