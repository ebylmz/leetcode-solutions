import heapq

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        """
        Time Complexity: O(n logn) - We perform heap operations (log n) up to n times in both directions
        Space Complexity: O(n) - Two heaps and two arrays of size n + 1
        """
        n = len(nums) // 3 # Total size = 3n, split into 3 equal parts

        # Compute left_sum[i] = min sum of n elements from nums[0 : n + i]
        max_heap = [-x for x in nums[:n]]   # Max-heap via negation
        heapq.heapify(max_heap)
        total_left = sum(nums[:n])
        left_sum = [0] * (n + 1)
        left_sum[0] = total_left

        for i in range(n, 2 * n):
            # Push current number and pop the largest to maintain smallest left_sum
            heapq.heappush(max_heap, -nums[i])
            total_left += nums[i]
            total_left -= -heapq.heappop(max_heap)
            left_sum[i - (n - 1)] = total_left # Index goes from 1 to n

        # Compute right_sum[i] = max sum of n elements from nums[n + i : ]
        min_heap = nums[2 * n:]
        heapq.heapify(min_heap)
        right_total = sum(nums[2 * n:])
        right_sum = [0] * (n + 1)        
        right_sum[n] = right_total

        for i in range(2 * n - 1, n - 1, -1):
            # Push current number and pop the smallest to maintain largest right_sum
            heapq.heappush(min_heap, nums[i])
            right_total += nums[i]
            right_total -= heapq.heappop(min_heap)
            right_sum[i - n] = right_total # Index goes from (n - 1) to 0

        # At split index i, compare left_sum[i] and right_sum[i]
        # left_sum[0] + right_sum[0] means keep the first n item as it is and remove n element from nums[n:]
        ans = float("inf")
        for sum1, sum2 in zip(left_sum, right_sum):
            ans = min(ans, sum1 - sum2)

        return ans


        """
             i
        [7,9,5,8,1,3]
         
        max_heap = [7,5]
        part1 = [16, 12, 12]

        min_heap = [5,8]
        part2 = [4,11,13]
        
        left_sum  = [16,12,12]
        right_sum = [4,11,13]
        
        """