class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        # Total time = O(n), where n is the number of nodes in the tree.
        # Total space = O(w), where w is the maximum width 
        
        # Idea 1: Ensure at least one node is present at each level
        # Idea 2: Use BFS, going left children first, and record the last (rightmost) node at each level
      
        if not root:
            return []

        right_view = []
        level = [root]
        # Apply BFS
        while level:
            next_level = []
            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)        
            
            right_view.append(level[-1].val)
            level = next_level
        return right_view
