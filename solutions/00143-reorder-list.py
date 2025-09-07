# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not head or not head.next:
            return

        # Step1: Find the middle node
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Split the list
        mid = slow.next
        slow.next = None

        # Step 2: Reverse the second half
        prev, curr = None, mid
        while curr:
            nxt = curr.next
            curr.next = prev
            prev, curr = curr, nxt

        # Step 3: Merge two halves
        l1, l2 = head, prev
        while l2: # len(l2) <= len(l1)
            tmp1, tmp2 = l1.next, l2.next
            l1.next = l2
            l2.next = tmp1 # tmp1 is either None or last node in last iteration
            l1, l2 = tmp1, tmp2