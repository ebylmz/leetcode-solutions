# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        less_dummy = ListNode()
        greater_dummy = ListNode()
        less, greater = less_dummy, greater_dummy

        curr = head
        while curr:
            if curr.val < x:
                less.next = curr
                less = less.next
            else:
                greater.next = curr
                greater = greater.next
            curr = curr.next

        # Terminate the greater list and link less list to greater
        greater.next = None
        less.next = greater_dummy.next

        return less_dummy.next