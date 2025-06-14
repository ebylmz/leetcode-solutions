class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        """
        IDEA: At each question, we can either solve it or skip it and try the next one. 
        To make the best decision, we look ahead to see which option gives us more total points.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        n = len(questions)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            points, jump = questions[i]
            next_index = i + jump + 1

            solve = points + (dp[next_index] if next_index < n else 0)
            skip = dp[i + 1]

            dp[i] = max(solve, skip)

        return dp[0]
