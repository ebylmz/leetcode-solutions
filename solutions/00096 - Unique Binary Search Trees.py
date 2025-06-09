class Solution:
    def numTrees(self, n: int) -> int:
        """
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        """

        numTree = [1] * (n + 1)

        # O node = 1 Tree
        # 1 node = 1 Tree
        for nodes in range(2, n + 1):
            total = 0
            for root in range(1, nodes + 1):
                left = root - 1
                right = nodes - root
                total += numTree[left] * numTree[right]
            numTree[nodes] = total
        
        return numTree[n]
