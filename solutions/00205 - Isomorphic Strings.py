class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if len(s) != len(t):
            return False
        
        transform = {}
        mapped = set()
        
        for curr, target in zip(s, t):
            if curr in transform:
                if transform[curr] != target:
                    return False
            else:
                # No two characters map to the same character
                if target in mapped:
                    return False
                transform[curr] = target
                mapped.add(target)

        return True
