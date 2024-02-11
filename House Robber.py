# House Robber
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
# code

class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1: return nums[0]
        p=[0]*(n+1)
        p[1]=nums[0]
        for i in range(1,n):
            p[i+1]=max(p[i-1]+nums[i], p[i])
        return p[n]
        