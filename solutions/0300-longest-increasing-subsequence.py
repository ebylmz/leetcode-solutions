from bisect import bisect_left

# Optimum solution
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        IDEA: Instead of tracking actual subsequences, track the 
        smallest tail of increasing subsequences of different lengths.
        Time Complexity: O(nlogn)
        Space Complexity: O(n)
        """
        lis = [] # lis[i] holds the smallest possible tail value of an increasing subsequence of length i + 1.
        for num in nums:
            i = bisect_left(lis, num)
            if i == len(lis):
                lis.append(num)
            else:
                lis[i] = num

        return len(lis)

# Easier to understand DP solution
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        """
        N = len(nums)
        dp = [1] * N 

        for i in range(N - 2, -1, -1):
            for j in range(i+1, N):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)