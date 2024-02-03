# Subsets II
# Given an integer array nums that may contain duplicates, return all possible 
# subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.
# code
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output, stack = [], []

        def backtrack(i):
            if i >= len(nums):
                output.append(stack.copy())
                return
            
            stack.append(nums[i])
            backtrack(i+1)

            stack.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            
            backtrack(i+1)
        
        backtrack(0)
        return output