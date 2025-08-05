"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if not node:
            return None

        node_new = Node(node.val)

        clones = {node.val: Node(node.val)}
        q = collections.deque([node])

        while q:
            curr = q.popleft()
            curr_clone = clones[curr.val] 
            for nei in curr.neighbors:
                if nei.val not in clones:
                    clones[nei.val] = Node(nei.val) 
                    q.append(nei)
                curr_clone.neighbors.append(clones[nei.val])
                        
        return clones[node.val]