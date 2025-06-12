from collections import Counter

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        """
            Time Complexity: O(n*logn), since we sort the nums array
            Space Complexity: O(1)
        """

        counts = Counter(nums)
        nums = sorted(list(set(nums)))
        
        earn1, earn2 = 0, 0
        for i in range(len(nums)):
            curr_earn = nums[i] * counts[nums[i]]
            if i > 0 and nums[i-1] == nums[i] - 1:
                curr_earn = max(earn1 + curr_earn, earn2)
            else:
                curr_earn += earn2
            earn1 = earn2
            earn2 = curr_earn

        return earn2  