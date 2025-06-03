class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        """
        IDEA: Use a monotonic decreasing stack to keep track of indices of days 
        with unresolved warmer temperatures.

        Time Complexity: O(n)
        Space Complexity: O(n) 
        """

        n = len(temperatures)
        stack = [0] # Stack stores indices of the temperatures list
        answer = [0] * n
        for i in range(1, n):
            # If the temperature at the top of the stack is greater than the current temperature,
            # then we know the current temperature is also lower than all others in the stack.
            # So, we simply append it to the stack as the new coldest (most recent) unresolved day.
            while stack and temperatures[i] > temperatures[stack[-1]]:
                p = stack.pop()
                answer[p] = i - p
            stack.append(i)

        return answer