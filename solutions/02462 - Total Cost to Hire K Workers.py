import heapq

class Solution(object):
    def totalCost(self, costs, k, c):
        """
        :type costs: List[int]
        :type k: int
        :type c: int
        :rtype: int

        IDEA:
        Use two min-heaps:
        - l_heap: smallest c elements from the left
        - r_heap: smallest c elements from the right

        Time: O(c + k * log c)
            - O(c) to build heaps
            - O(k log c) for up to k pop/push operations

        Space: O(c + k)
            - O(c) for heaps
            - O(k) for selected set
        """

        n = len(costs)
        selected = set()

        l_heap = [(costs[i], i) for i in range(c)]
        r_heap = [(costs[i], i) for i in range(n - c, n)] if c else []
        heapq.heapify(l_heap)
        heapq.heapify(r_heap)

        total_cost = 0
        l, r = c, n - c - 1

        for _ in range(min(k, n)):
            # Get smallest from either heap
            lv, rv = l_heap[0][0], r_heap[0][0]

            if lv <= rv:
                v, i = heapq.heappop(l_heap)
                # Avoid double-popping if the same item is at the top of r_heap
                if r_heap and i == r_heap[0][1]:
                    heapq.heappop(r_heap)
            else:
                v, i = heapq.heappop(r_heap)

            total_cost += v
            selected.add(i)

            # Refill left heap if space
            while l < n and len(l_heap) < c:
                if l not in selected:
                    heapq.heappush(l_heap, (costs[l], l))
                l += 1

            # Refill right heap if space
            while r >= 0 and len(r_heap) < c:
                if r not in selected:
                    heapq.heappush(r_heap, (costs[r], r))
                r -= 1

        return total_cost