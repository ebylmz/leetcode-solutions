# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        dp = {}

        def generate(start, end):
            if start > end:
                return [None]
            if (start, end) in dp:
                return dp[(start, end)]
                
            trees = []
            for i in range(start, end + 1):
                left_trees = generate(start, i - 1)
                right_trees = generate(i + 1, end)

                for left in left_trees:
                    for right in right_trees:
                        trees.append(TreeNode(i, left, right))
            dp[(start, end)] = trees
            return trees
            
        return generate(1, n)