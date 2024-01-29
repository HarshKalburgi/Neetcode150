#  Binary Tree Maximum Path Sum

# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

# The path sum of a path is the sum of the node's values in the path.

# Given the root of a binary tree, return the maximum path sum of any non-empty path.

#  code

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def findMaxPathSum(node):
            nonlocal maxi
            if not node:
                return 0
            left = max(findMaxPathSum(node.left), 0)
            right = max(findMaxPathSum(node.right), 0)
            maxi = max(maxi, left + right + node.val)
            return max(left, right) + node.val
        
        maxi = float('-inf')
        findMaxPathSum(root)
        return maxi