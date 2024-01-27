# Binary Tree Level Order Traversal
# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

#  code
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        
        def dfs(node, depth):
            if not node:
                return
            if depth >= len(ans):
                ans.append([])
            ans[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 0)
        return ans