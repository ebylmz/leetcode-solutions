from collections import Counter

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        """
        Time Complexity: O(n logn)
        Space Complexity: O(n)
        """
        counts1 = Counter(basket1)
        total_counts = counts1 + Counter(basket2)

        # Two baskets can be equal only if the total number of each fruit is even
        for c in total_counts.values():
            if c % 2 == 1:
                return -1

        fruits_to_swap = [] 
        for fruit, total_count in total_counts.items():
            target = total_count // 2
            diff = counts1.get(fruit, 0) - target
            # If diff > 0, b1 has a surplus. if diff < 0, b2 has a surplus.
            # abs(diff) is the number of items of this fruit type in the wrong basket.
            for _ in range(abs(diff)):
                fruits_to_swap.append(fruit)
        
        # Sort the fruits them to be swapped to swap the low cost fruit with high cost fruit
        fruits_to_swap.sort() 

        min_val = min(total_counts.keys())
        total_cost = 0
        # There are at least len(fruits_to_swap) // 2 swap needed
        for i in range(len(fruits_to_swap) // 2): 
            # Cost is min(direct swap cost, helper swap cost)
            total_cost += min(fruits_to_swap[i], 2 * min_val)

        return total_cost


        """
        [2,3]

        basket1 = [8, 1, 3, 2], 
        basket2 = [3, 1, 8, 2]

        """