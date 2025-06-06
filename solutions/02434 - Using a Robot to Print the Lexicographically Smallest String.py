class Solution(object):
    def robotWithString(self, s):
        """
        IDEA: Lexicographically smallest string starts with the smallest charachter 
        Time Complexity:  O(n), where n = len(s)
        Space Complexity: O(n)
        """
        n = len(s)
        
        # Precompute minimum suffix characters
        min_suf = [''] * n
        min_suf[-1] = s[-1]
        for i in range(n - 2, -1, -1):
            min_suf[i] = min(s[i], min_suf[i + 1])
        
        stack = []
        result = []
        
        for i in range(n):
            stack.append(s[i])
            
            # Look ahead to see the next min character left in s
            # Only pop if top of stack <= the min of the remaining s
            while stack and (i == n - 1 or stack[-1] <= min_suf[i + 1]):
                result.append(stack.pop())
        
        return ''.join(result)