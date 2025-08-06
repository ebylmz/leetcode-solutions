# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Time Complexity: O(n)
        Space Complexity: O(h) - where h is the height of the tree (recursion stack)
        """
        def dfs(node):
            if not node:
                return None

            # Flatten left and right subtrees
            left_tail = dfs(node.left)
            right_tail = dfs(node.right)
            
            # If there's a left subtree, we insert it between node and right subtree
            if left_tail:
                left_tail.right = node.right  # Connect tail of left to right
                node.right = node.left        # Move left subtree to the right
                node.left = None              # Set left to None

            # Return the tail of the flattened subtree
            return right_tail or left_tail or node

        return dfs(root)