class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        """
        Time Complexity: O(n*log n)
        Space Complexity: O(1)
        """
        INF = 10**20
        nums.sort()

        partitions = 0
        start = -INF
        for num in nums:
            if num - start > k:
                start = num
                partitions += 1
        
        return partitions