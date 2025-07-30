class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        num_set = set(nums)
        longest = 0

        for num in num_set:
            # Only start counting if 'num' is the beginning of a sequence
            if num - 1 not in num_set:
                curr = num
                streak = 1

                while curr + 1 in num_set:
                    curr += 1
                    streak += 1

                longest = max(longest, streak)

        return longest