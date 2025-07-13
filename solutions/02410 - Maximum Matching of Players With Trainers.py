class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        """
        Time Complexity : O(n log n + m log m), where n is the number of players and m is the number of trainers
        Space Complexity: O(1)
        """

        players.sort()
        trainers.sort()

        count = 0
        i = j = 0  # i for players, j for trainers

        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                count += 1
                i += 1
            j += 1

        return count
