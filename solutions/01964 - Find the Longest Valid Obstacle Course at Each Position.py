from bisect import bisect_right

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        """
        Time Complexity: O(n*logn)
        Space Complexity: O(n)
        """
        tails = [] # tails[i] = smallest ending value of subsequence of length i+1
        res = []

        for obs in obstacles:
            idx = bisect_right(tails, obs)
            if idx == len(tails):
                tails.append(obs)
            else:
                tails[idx] = obs
            res.append(idx + 1)
        return res