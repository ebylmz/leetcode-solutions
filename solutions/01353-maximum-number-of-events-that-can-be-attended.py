import heapq

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        """
        IDEA: 
            - We should process the events starting earliest to latest
            - We should select the event with earliest end 
            
        Time Complexity: O(n logn)
        Space Complexity: O(n)
        """
        # Sort events by start day
        n = len(events)
        events = sorted(events)
        # Find the last day for simulation
        last_day = max(end for _, end in events)
        
        heap = []        
        count, i = 0, 0
        for today in range(1, last_day + 1):
            # Add the end date of all events starting today
            while i < n and events[i][0] == today:
                heapq.heappush(heap, events[i][1])
                i += 1
            
            # Remove all the expired events
            while heap and heap[0] < today:
                heapq.heappop(heap)
            
            # Attend the event with earliest end
            if heap:
                heapq.heappop(heap)
                count += 1
            # Early stopping
            if i == n and heap is None:
                break
            
        return count