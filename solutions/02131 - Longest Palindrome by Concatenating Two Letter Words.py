from collections import Counter

class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        """
        words = ["lc","cl","gg"]
        counter = {"lc": 1, "cl": 1, "gg": 1}
        """

        # T(n) = O(n), S(n) = O(n), where n = len(words)

        matches = 0
        counts = Counter(words)
        for w in counts:
            if counts[w] > 0:
                rev_w = w[1] + w[0]
                if rev_w in counts:
                    if w != rev_w:
                        n = min(counts[w], counts[rev_w])
                        counts[w] -= n
                        counts[rev_w] -= n
                        matches += n
                    else:
                        matches += counts[w] // 2
                        counts[w] %= 2
        center = 0
        for w, c in counts.items():
            if c > 0 and w[0] == w[1]:
                center = 1
                break
        return matches * 4 + center * 2