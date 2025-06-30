class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)

        mx = 0
        for num, count in counts.items():
            if num + 1 in counts:
                mx = max(mx, count, count + counts[num + 1])
            if num - 1 in counts:
                mx = max(mx, count, count + counts[num + 1])
        return mx