class Solution(object):
    def numTilings(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        combs = [[None for _ in range(4)] for _ in range(n)]
        MOD = 10**9 + 7

        def get_state(t1, t2):
            if t1 and t2:
                return 0
            if not t1 and t2:
                return 1
            if t1 and not t2:
                return 2
            return 3

        """
        t1 | t3
        -------
        t2 | t4
        """

        def solve(i, t1, t2):
            if i == n:
                return 1
           
            state = get_state(t1, t2)
            if combs[i][state]:
                return combs[i][state]
           
            t3_t4 = i + 1 < n
            count = 0
            print(i,state)
            if state == 0: # (t1, t2) = (T, T)
                """
                X   XX  X   XX
                X   X   XX  XX
                """
                count += solve(i+1, True, True) 
                if t3_t4:
                    count += solve(i+1, False, True)
                    count += solve(i+1, True, False)
                    count += solve(i+1, False, False)
            elif state == 1: # (t1, t2) = (F, T)
                """
                #   #X
                XX  XX
                """
                if t3_t4: 
                    count += solve(i+1, True, False)
                    count += solve(i+1, False, False)
            elif state == 2: # (t1, t2) = (T, F)
                """
                XX  XX
                #   #X
                """
                if t3_t4: 
                    count += solve(i+1, False, True)
                    count += solve(i+1, False, False)
            else: # state == 3 # (t1, t2) = (F, F)
                # Just continue on the next column
                count += solve(i+1, True, True)       

            combs[i][state] = count % MOD
            return combs[i][state]

        return solve(0, True, True) % MOD