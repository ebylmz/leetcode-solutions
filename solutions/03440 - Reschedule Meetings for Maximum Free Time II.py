from bisect import bisect_left

class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        """
        Intuition: To maximize free time, we need to consider the gaps between events, 
        and how we can combine them with the duration of the event being scheduled.
        
        Time Complexity: O(n log n), since we sort the free times and use binary search.
        Space Complexity: O(n), for storing the free times and their indices.
        """

        free_times = []

        # Calculate all free time intervals between events
        free_times.append(startTime[0])
        for i in range(len(startTime) - 1):
            free_times.append(startTime[i + 1] - endTime[i]) 
        free_times.append(eventTime - endTime[-1])

        # Pre-sort free times with original indices for binary search
        sorted_free_times = sorted([(v, i) for i, v in enumerate(free_times)], key=lambda x: x[0])        
        
        n = len(free_times)
        best = 0
        for i in range(n - 1):
            combined_free = free_times[i] + free_times[i + 1]
            event_duration = endTime[i] - startTime[i]
            idx = bisect_left(sorted_free_times, event_duration, key=lambda x: x[0])
            
            # Skip intervals overlapping with current pair
            while idx < n and sorted_free_times[idx][1] in (i, i + 1):
                idx += 1
            
            # If found, include this interval as well
            if idx < n:
                combined_free += event_duration
            best = max(best, combined_free)
        
        return best