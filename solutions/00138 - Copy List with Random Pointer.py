"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Time Complexity: O(n) - Traverses the list twice
        Space Complexity: O(n) - Keeping the mappings between old and new nodes
        """

        if not head:
            return None

        old_to_new = {}

        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            old_to_new[curr].next = old_to_new.get(curr.next, None)    
            old_to_new[curr].random = old_to_new.get(curr.random, None)    
            curr = curr.next
        
        return old_to_new[head]