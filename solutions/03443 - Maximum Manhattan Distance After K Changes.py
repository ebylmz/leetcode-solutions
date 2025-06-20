class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        """
        IDEA: Track direction counts and calculate max distance on each step.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        counts = {'N': 0, 'S': 0, 'W': 0, 'E': 0}

        best = 0
        for c in s:
            remaining_k = k
            counts[c] += 1

            # Horizontal direction (E-W)
            x_max = max(counts['W'], counts['E'])
            x_min = min(counts['W'], counts['E'])

            used = min(x_min, remaining_k)
            x_min -= used
            x_max += used
            remaining_k -= used
            
            # Vertical direction (N-S)
            y_max = max(counts['N'], counts['S'])
            y_min = min(counts['N'], counts['S'])

            used = min(y_min, remaining_k)
            y_min -= used            
            y_max += used            

            best = max(best, x_max - x_min + y_max - y_min)

        return best