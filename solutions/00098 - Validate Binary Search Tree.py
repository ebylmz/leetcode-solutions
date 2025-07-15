# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_bst(node, low, high):
            """
            Time Complexity: O(n) - Visits each node once.
            Space Complexity: O(h) - Recursion stack, where h is the height of the tree
            """
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return is_bst(node.left, low, node.val) and is_bst(node.right, node.val, high)
        
        return is_bst(root, float('-inf'), float('inf'))