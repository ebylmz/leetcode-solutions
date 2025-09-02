class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        """
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        n = len(points)
        # Sort points:
        # - primarily by x in ascending order (A will always be left of B)
        # - secondarily by y in descending order (To have the high point first).
        points.sort(key=lambda p: (p[0], -p[1]))
        count = 0
        for i in range(n - 1):
            y = points[i][1]
            high = -1 # Highest y value smaller or equal to y
            for j in range(i + 1, n):
                if high < points[j][1] <= y:
                    count += 1
                    high = points[j][1]
                    if high == y: # It will always be in the upper border
                        break
        return count