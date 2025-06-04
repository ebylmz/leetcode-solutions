class Solution(object):
    def answerString(self, word, numFriends):
        """
        IDEA: Try each substring starts with the lexicographically largest letter
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        
        if numFriends == 1:
            return word
        
        n = len(word)
        max_len = n - numFriends + 1
        max_char = max(word)
        best = ""
        for start in range(n):
            if word[start] == max_char:
                end = min(start + max_len, n)
                candidate = word[start:end]
                if candidate > best:
                    best = candidate
        return best
