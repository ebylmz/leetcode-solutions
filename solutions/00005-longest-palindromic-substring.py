class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """

        N = len(s)

        def get_max_palindrom(l, r):
            length = 0
            while l >= 0 and r < N and s[l] == s[r]:
                l -= 1
                r += 1
            l, r = l + 1, r - 1
            return l, r, r - l + 1

        start, end, max_len = 0, 0, 0
        for i in range(N - 1):
            # Odd length palindrom
            l, r, curr_len = get_max_palindrom(i, i)
            if curr_len > max_len:
                start, end, max_len = l, r, curr_len
            # Even length palindrom
            l, r, curr_len = get_max_palindrom(i, i + 1)
            if curr_len > max_len:
                start, end, max_len = l, r, curr_len
        
        return s[start:end + 1]