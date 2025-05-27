class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # T(n) = O(n), S(n) = O(1)

        """
        Idea: Keep the left and rigth summation of the numbers
        
        nums=[2,1,-1]
        lsum=0,2,3
        rsum=0,-1,0
        
        nums=[1,2,3]
        lsum=0,1,3
        rsum=5,3,0
        """

        n = len(nums)
        lsum = 0 
        rsum = sum(nums)
        for i in range(len(nums)):
            rsum -= nums[i]
            if lsum == rsum:
                return i
            lsum += nums[i]

        return -1