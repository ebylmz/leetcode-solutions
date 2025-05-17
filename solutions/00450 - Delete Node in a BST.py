# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """

        # Deletion cases:
        # 1. Node has no children – return None.
        # 2. Node has one child – return that child.
        # 3. Node has two children – replace node value with inorder successor
        #    (smallest value in right subtree), then delete the successor.
        
        # Time Complexity: O(height of tree)
        # Space Complexity: O(height of tree) due to recursion stack        
        
        def remove_node(root, key):
            if not root:
                return None
            
            if key < root.val:
                root.left = remove_node(root.left, key)
            elif key > root.val:
                root.right = remove_node(root.right, key)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                else:
                    # Find inorder successor (smallest in the right subtree)
                    successor = root.right
                    while successor.left:
                        successor = successor.left
                    root.val = successor.val
                    root.right = remove_node(root.right, successor.val)
            return root
        
        return remove_node(root, key)