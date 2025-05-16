class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        n = len(senate) # Use it as offset
        dire, radiant = deque(), deque()

        for i in range(n):
            if senate[i] == 'D':
                dire.append(i)
            else:
                radiant.append(i)
        
        while dire and radiant:
            d = dire.popleft()
            r = radiant.popleft()

            # First coming senate bans the closest rival senate
            if d < r:
                dire.append(d + n) 
            else:
                radiant.append(r + n)
        
        return "Dire" if dire else "Radiant"

