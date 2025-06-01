class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        """
        Time Complexity (Worst Case): O(n**2)
        Time Complexity (Average): O(n*logn)
        Space Complexity: O(1)
        """

        target = len(nums) - k  # convert to k-th smallest

        def quickSelect(left, right):
            if left == right:
                return nums[left]

            less, equal, greater, pivot = left, left, right, nums[right]
            while equal <= greater:
                if nums[equal] < pivot:
                    nums[less], nums[equal] = nums[equal], nums[less]
                    less += 1
                    equal += 1
                elif nums[equal] == pivot:
                    equal += 1
                else:  # nums[equal] > pivot
                    nums[equal], nums[greater] = nums[greater], nums[equal]
                    greater -= 1

            # Decide which side to recurse into
            if target < less:
                return quickSelect(left, less - 1)
            elif target > greater:
                return quickSelect(greater + 1, right)
            else:
                return pivot

        return quickSelect(0, len(nums) - 1)
