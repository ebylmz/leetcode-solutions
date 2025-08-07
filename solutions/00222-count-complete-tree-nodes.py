# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        """
        Time Complexity: O(log^2 n)
        Space Complexity: O(log n) — due to recursion stack in the worst case.
        """

        def compute_left_height(node):
            height = 0
            while node:
                node = node.left
                height += 1
            return height

        def compute_right_height(node):
            height = 0
            while node:
                node = node.right
                height += 1
            return height

        def count(node):
            if not node:
                return 0
            
            left_height = compute_left_height(node)
            right_height = compute_right_height(node)
            
            if left_height == right_height:
                # It's a perfect binary tree.
                return (2 ** left_height) - 1
            else:
                # Recursively count left and right subtrees
                return 1 + count(node.left) + count(node.right)

        return count(root)