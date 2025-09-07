class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        result = []
        i, n = 0, len(intervals)

        # Step 1: Add all intervals before newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        # Step 2: Merge overlapping intervals with newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        
        result.append(newInterval)

        # Step 3: Add the rest
        result.extend(intervals[i:])

        return result