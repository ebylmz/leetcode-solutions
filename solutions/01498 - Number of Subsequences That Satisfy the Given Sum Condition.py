from bisect import bisect_right

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        """
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        MOD = 10 ** 9 + 7
        n = len(nums)
        nums.sort()

        # Precompute powers of 2 modulo MOD
        power = [1] * n
        for i in range(1, n):
            power[i] = (power[i - 1] * 2) % MOD

        count = 0
        for i in range(n):
            max_val = target - nums[i]
            if max_val < nums[i]:
                break # No valid subsequences can be formed with nums[i] as the smallest
            # Find rightmost index where nums[j] <= max_val
            j = bisect_right(nums, max_val, i + 1)
            # number of possible sequences starting with nums[i]: max sequence lenght - 1
            count = (count + power[j - i - 1]) % MOD
        return count
