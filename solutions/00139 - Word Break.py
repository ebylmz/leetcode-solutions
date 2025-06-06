class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        """
        IDEA: dp[i] represents whether the substring s[i:] can be segmented into words from the dictionary.
    
        # Time Complexity: O(n * k), where n = len(s), k = average length of words in wordDict
        #   - For each position i in the string, we check all words in the dictionary.
        # Space Complexity: O(n), where n = len(s) for the dp array
        """

        wordDict = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True # Empty string is considered segmentable

        for i in range(n - 1, -1, -1):
            for w in wordDict:
                m = len(w)
                if i + m <= n and s[i:i+m] in wordDict:
                    dp[i] = dp[i+m]
                    if dp[i]:
                        break
        return dp[0]