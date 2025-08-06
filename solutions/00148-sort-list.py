# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time Complexity: O(n logn)
        Space Complexity: O(n logn) - due to recursion stack
        """
        def get_mid(head):
            if not head or not head.next:
                return head, head
            
            slow, fast = head, head
            while fast and fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next

            mid = slow.next
            slow.next = None
            return mid
        
        def merge(l1, l2):
            curr = dummy = ListNode() # Dummy head
            
            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            
            curr.next = l1 if l1 else l2
            
            return dummy.next

        def merge_sort(head):
            if not head or not head.next:
                return head
            
            # Partition the list from half
            mid = get_mid(head)

            # Sort the partitions
            left = merge_sort(head)
            right = merge_sort(mid)
            
            # Merge the sorted partitions
            return merge(left, right)

        return merge_sort(head)