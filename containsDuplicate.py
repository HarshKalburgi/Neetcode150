# 1)contains duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# program
class solution:
    def duplicate(self,nums):
        hashset=set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False