class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        """
        To form a triangle with three sides a, b, c (a <= b <= c), 
        the triangle inequality rule reduces to: a + b > c.

        Time Complexity: O(n^2)
        Space Complexity: O(n)
        """
        # Sort the array so that we can assume a <= b <= c
        nums_sorted = sorted(nums)

        count = 0
        # Iterate from the largest side to the smallest
        for i in range(len(nums_sorted) - 1, -1, -1):
            # nums_sorted[i] is considered as the largest side 'c'
            left, right = 0, i - 1
            # Use two pointers to find all valid pairs (a, b) with a + b > c
            while left < right:
                if nums_sorted[left] + nums_sorted[right] > nums_sorted[i]:
                    # If a + b > c, then all pairs between left and right are valid
                    count += right - left
                    # Move the right pointer to find more pairs with the next smaller b
                    right -= 1
                else:
                    # If the sum is not enough, move the left pointer to try a larger a
                    left += 1
        return count