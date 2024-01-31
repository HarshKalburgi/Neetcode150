# Kth Largest Element in an Array
# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?

# code
class Solution:
    def findKthLargest(self, nums, k):
        return sorted(nums, reverse=True)[k-1]
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        