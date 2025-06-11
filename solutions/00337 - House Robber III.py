# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        """
            Time Complexity: O(n), Each node visited exactly once
            Space Complexity: O(logn) for a balance tree and O(n) for a skewed tree
        """

        def dfs(node):
            if node is None:
                return (0, 0) # (not_rob_this_node, rob_this_node)
            
            left = dfs(node.left)
            right = dfs(node.right)

            rob = node.val + left[0] + right[0]
            not_rob = max(left) + max(right)

            return (not_rob, rob)
        
        return max(dfs(root))