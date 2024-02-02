# Combination Sum

# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
# frequency
#  of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
# code

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(n=0,a=[],b=0):
            if b==target:
                l.append(a[:])
                return
            elif b>target:
                return
            
            for i in range(n, len(candidates)):
                a.append(candidates[i])
                b+=candidates[i]
                
                backtrack(i,a,b)
                
                a.pop()
                b-=candidates[i]                
        l=[]
        backtrack()
        return l