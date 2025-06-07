class Solution:
    def clearStars(self, s: str) -> str:
        """
        IDEA: Maintain a min heap and pop the smallest leftmost 
        charachter, when encountered with a star
        Time Complexity: O(n * logn)
        Space Complexity: O(n)
        """

        N = len(s)
        h = []

        for i in range(N):
            if s[i] == "*":
                v, index = heapq.heappop(h)
            else:
                # Add negative of index value, in order to get the leftmost smallest char
                heapq.heappush(h, (s[i], -i))
        
        remained = [False] * N
        while h:
            _, index = heapq.heappop(h)
            remained[-index] = True
        
        return ''.join([s[i] for i in range(N) if remained[i]])
            