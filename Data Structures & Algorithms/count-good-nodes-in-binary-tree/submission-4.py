# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:


        def dfs(node,max_value):
            if node is None:
                return 0

            good = 1 if node.val >= max_value else 0

            max_value = max(max_value,node.val)
            left_child = dfs(node.left,max_value)
            right_child = dfs(node.right,max_value)


            return good+left_child+right_child


        return dfs(root,root.val)
        