from heapq import heappush, heappop

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """
        Time Complexity: O(k logk)
        Space Complexity: O(k)
        """
        if not nums1 or not nums2:
            return []
        
        res = []
        visited = set()
        heap = [(nums1[0] + nums2[0], 0, 0)]
        visited.add((0, 0))

        while len(res) < k and heap:
            _, i, j = heappop(heap)
            res.append((nums1[i], nums2[j]))
            if i + 1 < len(nums1) and (i + 1, j) not in visited:
                heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
                visited.add((i + 1, j))

            if j + 1 < len(nums2) and (i, j + 1) not in visited:
                heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
                visited.add((i, j + 1))
            
        return res