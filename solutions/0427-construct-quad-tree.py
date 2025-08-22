"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        """
        Time Complexity: O(n^2 * logn)
        Space Complexity: O(logn)
        """
        n = len(grid)
        
        def is_uniform(r1, r2, c1, c2):
            """Check if subgrid [r1:r2+1, c1:c2+1] contains all the same values"""
            val = grid[r1][c1]
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    if grid[r][c] != val:
                        return False, None
            return True, val

        def dfs(r1, r2, c1, c2):
            uniform, val = is_uniform(r1, r2, c1, c2)
            if uniform:
                return Node(val, True)

            rm, cm = (r1 + r2) // 2, (c1 + c2) // 2
            return Node(
                val=1,  # doesn’t matter for non-leaf
                isLeaf=False,
                topLeft=dfs(r1, rm, c1, cm),
                topRight=dfs(r1, rm, cm + 1, c2),
                bottomLeft=dfs(rm + 1, r2, c1, cm),
                bottomRight=dfs(rm + 1, r2, cm + 1, c2)
            )

        return dfs(0, n - 1, 0, n - 1)