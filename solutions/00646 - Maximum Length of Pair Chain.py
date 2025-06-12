class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        """
        Time Complexity: O(n*logn)
        Space Complexity: O(1)
        """
        pairs.sort(key=lambda x: x[1])
        n = len(pairs)

        length, end = 1, pairs[0][1]
        for i in range(1, n):
            if pairs[i][0] > end:
                length += 1
                end = pairs[i][1]
        
        return length
