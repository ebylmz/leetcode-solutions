import heapq

class Solution(object):
    def maxScore(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        
        """
        T(n) = O(n*logn), due to sorting O(n*logn) and heapify operation O(n*log(n))
        S(n) = O(n), due to pairs array and heap
        """

        pairs = [(nums1[i],  nums2[i]) for i in range(len(nums2))]
        pairs.sort(key=lambda x: x[1], reverse=True)
        
        heap = []
        max_score = curr_sum = 0
        for n1, n2 in pairs:
            heapq.heappush(heap, n1)
            curr_sum += n1
            if len(heap) > k:
                curr_sum -= heapq.heappop(heap)
            # n2 is smallest for sure
            if len(heap) == k:
                max_score = max(max_score, curr_sum * n2)
        
        return max_score
    

    """
    nums1 = [4,2, 3,1,1] 
    nums2 = [7,5,10,9,6]
    pairs = [(10,3),(1,9),(4,7),(1,6),(2,5)]
                                  i
    heap = [2, 4, 10]
    curr_sum = 16
    max_score = max(15 * 7, 16 * 5)
    """