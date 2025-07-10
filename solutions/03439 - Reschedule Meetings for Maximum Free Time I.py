class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        intervals = []
        intervals.append(startTime[0] - 0)
        for i in range(len(startTime) - 1):
            intervals.append(startTime[i + 1] - endTime[i])
        intervals.append(eventTime - endTime[-1])

        prefix_sum = [0] * (len(intervals) + 1)
        for i in range(len(intervals)):
            prefix_sum[i + 1] = prefix_sum[i] + intervals[i]

        best = 0
        for i in range(k + 1, len(prefix_sum)):
            best = max(best, prefix_sum[i] - prefix_sum[i - (k + 1)])

        return best