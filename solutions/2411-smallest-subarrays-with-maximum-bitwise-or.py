class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        """
        Time Complexity: O(n * 32) = O(n)
        Space Complexity: O(32) = O(1)
        """
        n = len(nums)
        last_seen = [-1] * 32  # last index seen for each bit (0–31) since nums[i] <= 10^9
        ans = [1] * n
        max_or = 0

        for i in range(n - 1, -1, -1):
            num = nums[i]
            max_or |= num
            target = max_or
            bit = 0

            # For each bit set in max_or, update last seen and required length
            while target:
                if num & 1:
                    last_seen[bit] = i  # current bit seen at index i
                elif last_seen[bit] != -1:
                    # bit was seen later, so extend the window to include it
                    ans[i] = max(ans[i], last_seen[bit] - i + 1)
                num >>= 1
                target >>= 1
                bit += 1

        return ans