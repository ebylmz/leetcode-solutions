# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        if not head or left == right:
            return head
        
        dummy = ListNode(0, head)
        left_prev = dummy

        # Reach node at position left
        for _ in range(left - 1):
            left_prev = left_prev.next
        curr = left_prev.next

        # Reverse from left to right
        prev = None
        for _ in range(right - left + 1):
            tmp_next = curr.next
            curr.next = prev
            prev = curr
            curr = tmp_next
        
        left_prev.next.next = curr # curr is node after right
        left_prev.next = prev # prev is right
        
        return dummy.next


        """
             l         r
        1 -> 2 -> 3 -> 4 -> 5
                       p
                            c
        """
