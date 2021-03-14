# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        def BFS(root):
            if not root:
                return
            BFS(root.left)
            res.append(root.val)
            BFS(root.right)

        res = []
        BFS(root)
        return res
