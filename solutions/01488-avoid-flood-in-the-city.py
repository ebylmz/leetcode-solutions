import heapq

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        """
        Time Complexity: O(n * log(n)), each rain/dry operation may push/pop from heap.
        Space Complexity: O(n)
        """
        ans = [-1] * len(rains)
        next_rain = collections.defaultdict(list)

        # Record the future days for each lake
        for day, lake in enumerate(rains):
            if lake > 0:
                next_rain[lake].append(day)
        
        full_lakes = set()
        heap = [] # (next_rain_day, lake)

        for i, lake in enumerate(rains):
            if lake > 0:
                # Remove today from its future list
                next_rain[lake].pop(0)

                # Flood check
                if lake in full_lakes:
                    return []
                full_lakes.add(lake)

                # If lake will rain again, schedule a drying
                if next_rain[lake]:
                    next_day = next_rain[lake][0]
                    heapq.heappush(heap, (next_day, lake))
            else:
                if heap:
                    # Dry the lake that will rain soonest
                    next_day, lake_to_dry = heapq.heappop(heap)
                    full_lakes.remove(lake_to_dry)
                    ans[i] = lake_to_dry
                else:
                    ans[i] = 1 # arbitrary placeholder, any valid lake number works
        
        return ans