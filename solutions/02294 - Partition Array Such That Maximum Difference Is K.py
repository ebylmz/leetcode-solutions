class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        """
        Time Complexity: O(n log n)
        Space Complexity: O(1)
        """
        nums.sort()
        partitions = 1
        start = nums[0]
        
        for num in nums:
            if num - start > k:
                start = num
                partitions += 1
        
        return partitions