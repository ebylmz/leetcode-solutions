import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        """
        Time Complexity: O(n + klogn), where n is the number of classes and k is the number of extra student
        Space Complexity: O(n)
        """

        def gain(pass_i, total_i):
            return (pass_i + 1) / (total_i + 1) - pass_i / total_i

        heap = []
        for pass_i, total_i in classes:
            # Push the negative gain
            heapq.heappush(heap, (-gain(pass_i, total_i), pass_i, total_i))

        for _ in range(extraStudents):
            neg_gain, pass_i, total_i = heapq.heappop(heap)
            pass_i += 1
            total_i += 1
            heapq.heappush(heap, (-gain(pass_i, total_i), pass_i, total_i))
        
        total = 0.0
        while heap:
            _, pass_i, total_i = heapq.heappop(heap)
            total += pass_i / total_i
        return total / len(classes)