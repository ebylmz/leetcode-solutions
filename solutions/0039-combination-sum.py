class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i: int, current: List[int], remaining: int):
            if remaining == 0:
                res.append(current[:])
                return
            if i == len(candidates) or remaining < 0:
                return

            # Include current candidate (can reuse the same one)
            current.append(candidates[i])
            dfs(i, current, remaining - candidates[i])
            current.pop()

            # Skip current candidate
            dfs(i + 1, current, remaining)

        dfs(0, [], target)
        return res