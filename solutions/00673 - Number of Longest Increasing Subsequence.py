class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        """
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        """
        n = len(nums)
        lengths = [1] * n  # lengths[i] = length of LIS ending at nums[i]
        counts = [1] * n   # counts[i] = number of LISs ending at nums[i]

        max_len, max_count = 0, 0
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    if lengths[j] + 1 > lengths[i]:
                        lengths[i], counts[i] = lengths[j] + 1, counts[j]
                    elif lengths[j] + 1 == lengths[i]:
                        counts[i] += counts[j]
            if lengths[i] > max_len:
                max_len, max_count = lengths[i], counts[i]
            elif lengths[i] == max_len:
                max_count += counts[i]
                    
        return max_count