# Longest Consecutive Sequence
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.
# code

class Solution(object):
    def longestConsecutive(self, nums):
        numSet = set(nums)
        longest = 0

        for n in nums:
            if(n-1) not in numSet:
                length = 0
                while (n+length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest