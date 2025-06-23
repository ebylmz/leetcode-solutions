class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """
        Time Complexity: O(n*logn)
        Space Complexity: O(n)
        """

        # Sort by width ascending and height descending
        # Sorting by height descending for envelopes with the same width ensures 
        # you don't count envelopes of the same width twice in the LIS step
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        lis = []

        # Find LIS in heights using binary search
        for _, h in envelopes:
            i = bisect.bisect_left(lis, h)
            if i == len(lis):
                lis.append(h)
            else:
                lis[i] = h

        return len(lis)