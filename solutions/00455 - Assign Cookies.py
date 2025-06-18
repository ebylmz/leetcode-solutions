class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """
        Time Complexity: O(n*logn)
        Time Complexity: O(1)
        """
        g.sort()
        s.sort()

        total, child, cookie = 0, 0, 0 
        while cookie < len(s) and child < len(g):
            if s[cookie] >= g[child]:
                child += 1
            cookie += 1
        return child