# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.height = 0

        def dfs(node):
            if node is None:
                return 0
            else:
                left = dfs(node.left)
                right = dfs(node.right)
                left_path = right_path = 0
                if node.left and node.left.val == node.val:
                    left_path = left + 1
                if node.right and node.right.val == node.val:
                    right_path = right + 1
                self.height = max(self.height, left_path + right_path)
                return max(left_path, right_path)

        dfs(root)
        return self.height
