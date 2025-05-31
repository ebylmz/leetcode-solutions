class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        """
        IDEA: Ajust the right and left boundaries with the constrain at most k zeros in it
        T(n) = O(n)
        S(n) = O(1)
        """

        """
        num_zeros = 1
                             r
        [1,1,1,0,0,0,1,1,1,1,0]
                   l
        """

        l = 0
        zeros = 0
        max_len = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                num_zeros += 1
            
            # Adjust the window if needed
            while num_zeros > k and l <= r:
                if nums[l] == 0:
                    num_zeros -= 1
                l += 1
            w = r - l + 1
            max_len = max(max_len, w)
            
        return max_len