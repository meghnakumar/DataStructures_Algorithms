# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode, res=1) -> int:
        result = 0
        stk = [(root, root.val)]
        while stk:
            node, curr_max = stk.pop()
            if not node:
                continue
            curr_max = max(curr_max, node.val)
            result += int(curr_max <= node.val)
            stk.append((node.right, curr_max))
            stk.append((node.left, curr_max))
        return result
        

        