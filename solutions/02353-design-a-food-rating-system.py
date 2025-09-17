import heapq

class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        """
        Time Complexity: O(n logn)
        Space Complexity: O(n)
        """
        self.food_to_cuisine = {}
        self.food_to_rating = {}
        self.cuisine_to_heap = collections.defaultdict(list)
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_to_cuisine[food] = cuisine
            self.food_to_rating[food] = -rating
            heapq.heappush(self.cuisine_to_heap[cuisine], (-rating, food))
        
    def changeRating(self, food: str, newRating: int) -> None:
        """
        Update the rating of a food and push new entry into the heap.
        Time Complexity: O(log k), where k = number of foods in this cuisine
        """
        cuisine = self.food_to_cuisine[food]
        heapq.heappush(self.cuisine_to_heap[cuisine], (-newRating, food))   
        self.food_to_rating[food] = -newRating      

    def highestRated(self, cuisine: str) -> str:
        """
        Time Complexity: Amortized O(log k) due to lazy deletion.
        """
        if cuisine not in self.cuisine_to_heap:
            return ""

        # Lazy deletion: remove stale entries
        heap = self.cuisine_to_heap[cuisine]
        while heap[0][0] != self.food_to_rating[heap[0][1]]: # heap[0]: (-rating, food)
            heapq.heappop(heap)  # discard outdated entry
   
        return heap[0][1]