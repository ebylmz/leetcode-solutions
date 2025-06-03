class StockSpanner(object):

    def __init__(self):
        self.stack = []

    def next(self, price):
        """
        IDEA: When the current price is greater than or equal to 
        the price at the top of the stack, we pop the stack and add its span to the current span.
        This process continues until we find a higher price or the stack is empty.
        
        Time Complexity: O(1) amortized per call to next(), O(n) total for n calls.
        Space Complexity: O(n) in the worst case (all prices strictly decreasing).
        """
        span = 1
        while self.stack and price >= self.stack[-1][0]:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        
        return span
