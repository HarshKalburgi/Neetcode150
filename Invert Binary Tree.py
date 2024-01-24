# Invert Binary Tree
# Given the root of a binary tree, invert the tree, and return its root.

# code
class Solution(object):
    def invertTree(self, root):
        # Base case...
        if root == None:
            return root
        # swapping process...
        root.left, root.right = root.right, root.left
        # Call the function recursively for the left subtree...
        self.invertTree(root.left)
        # Call the function recursively for the right subtree...
        self.invertTree(root.right)
        return root     # Return the root...