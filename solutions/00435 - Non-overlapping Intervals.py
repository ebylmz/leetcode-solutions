class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        """
        IDEA: Always select the next possible event that ends as early as possible. 

        T(n) = O(nlog(n)), due to sorting algorithm
        S(n) = O(1)
        """
        
        intervals.sort(key = lambda x: x[1])

        remove = 0
        prev_end = intervals[0][0]
        for start, end in intervals:
            # If the current event starts before the previous event finished,
            # Then there must be an overlapping because due to sorting we are 
            # sure that end >= prev_end
            if start < prev_end: # Overlapping
                remove += 1
            else:
                prev_end = end
        return remove
