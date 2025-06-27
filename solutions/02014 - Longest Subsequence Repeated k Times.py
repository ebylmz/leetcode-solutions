class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        """
        IDEA: Use BFS
        Time Complexity: O(a^{n//k} * n), a = number of unique characters in s 
        Space Complexity: O(a^{n//k} * (n//k))
        """
        
        def count_subseq(curr):
            i = 0
            count = 0
            for c in s:
                if c == curr[i]:
                    i += 1
                    if i == len(curr):
                        i = 0
                        count += 1
            return count
        
        cs = sorted(set(s)) # Sort for lexicographically largest subsequence
        q = collections.deque()
        q.append("")

        best = ""
        while q:
            curr = q.popleft()

            for c in cs:
                if count_subseq(curr + c) >= k:
                    q.append(curr + c)
            
            # The last string in q is the longest subsequence repeated k times
            best = curr
        
        return best