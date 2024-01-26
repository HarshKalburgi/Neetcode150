#  Subtree of Another Tree
# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

# code:

class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """ 
        if root is None and subRoot is None:
            return True
        if subRoot is None:
            return True
        if root is None and subRoot is not None:
            return False
        return self.isSame(root,subRoot) or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

    def isSame(self,root,subRoot):
        if root is None and subRoot is None:
            return True
        if root is None or subRoot is None:
            return False
        return root.val == subRoot.val and self.isSame(root.left,subRoot.left) and self.isSame(root.right,subRoot.right)