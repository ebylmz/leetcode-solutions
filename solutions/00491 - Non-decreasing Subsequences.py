from typing import List

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = set()

        def dfs(i: int, curr_seq: List[int]):
            if len(curr_seq) >= 2:
                result.add(tuple(curr_seq)) 

            if i == len(nums):
                return

            # Case 1: Include nums[i] if it's non-decreasing
            if not curr_seq or curr_seq[-1] <= nums[i]:
                dfs(i + 1, curr_seq + [nums[i]])

            # Case 2: Skip nums[i]
            dfs(i + 1, curr_seq)

        dfs(0, [])
        return [list(seq) for seq in result]
