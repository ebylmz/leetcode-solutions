# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        Time Complexity: O(n), each node is visited once
        Space Complexity: O(h), where h is the height of the tree. O(n) in the worst case
        """
        self.mx = root.val

        def dfs(node):
            if not node:
                return 0

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))
            self.mx = max(self.mx, node.val + left + right)

            return node.val + max(left, right)

        dfs(root)
        return self.mx