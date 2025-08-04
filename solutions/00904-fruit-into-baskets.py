from collections import Counter

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        Sliding window approach to find the longest subarray
        with at most 2 distinct fruit types.

        Time Complexity: O(n)
        Space Complexity: O(1) — since number of fruit types is bounded
        """
        count = Counter()
        left = max_fruits = 0

        for right, fruit in enumerate(fruits):
            count[fruit] += 1

            while len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]
                left += 1

            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits