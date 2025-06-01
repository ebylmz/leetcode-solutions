class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        """
        IDEA: Balloons can be burst together if they share a common region on the x-axis.

        We place the first arrow at the end of the first balloon to maximize 
        how many overlapping balloons we can burst with that single shot.

        As we iterate, if we encounter a balloon that starts after the current 
        arrow position (meaning no overlap), we fire an arrow to burst the previous 
        group and update the arrow position to the end of the current balloon.
        
        T(n) = O(nlog(n)), due to sorting algorithm
        S(n) = O(1)
        """

        points.sort(key = lambda x: x[1])
        arrow = points[0][1] # Initial poisiton of arrow
        shots = 1            # Initially we have a single arrow
        for start, end in points:
            if start > arrow:
                shots += 1
                arrow = end
        return shots