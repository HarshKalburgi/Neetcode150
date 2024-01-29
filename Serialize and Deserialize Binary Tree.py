# Serialize and Deserialize Binary Tree

# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

# Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

# code
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """ O(N)TS LC297 """
        return str(root.val) + ',' + self.serialize(root.left) + ',' + self.serialize(root.right) if root else "None"

    def deserialize(self, data):
        """ O(N)TS LC297 """

        def fn():
            if (n := arr.pop()) != 'None':
                return TreeNode(int(n), fn(), fn())

        arr = data.split(',')[::-1]
        return fn()