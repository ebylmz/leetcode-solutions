class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Time Complexity: O(n! * n^2), n! possibilities, and each permuation takes O(n^2) due to list creation
        Space Complexity: O(n! * n), n! possibilites each of lenght n
        """
        n = len(nums)
        if n == 0:
            return [[]]

        res = []
        perms = self.permute(nums[1:])
        for p in perms:
            for i in range(n):
                res.append(p[:i] + [nums[0]] + p[i:])
        
        return res