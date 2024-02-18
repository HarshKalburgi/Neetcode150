# Burst Balloons
# You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.
# If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.
# Return the maximum coins you can collect by bursting the balloons wisely.
# code

#Recursion 
#Time Complexity: O(Exponential)
#Space Complexity: O(n)
class Solution1:
    def maxCoins(self, nums: List[int]) -> int:
        def solve(i,j):
            if i>j:
                return 0
            maxi=-maxsize
            for k in range(i,j+1):
                coins=nums[i-1]*nums[k]*nums[j+1]+solve(i,k-1)+solve(k+1,j)
                maxi=max(maxi,coins)
            return maxi
        
        n=len(nums)
        nums.insert(0,1)
        nums.append(1)
        return solve(1,n)
    
#Memoization (Top-Down)
#Time Complexity: O(n^3)
#Space Complexity: O(n^2) + O(n)
class Solution2:
    def maxCoins(self, nums: List[int]) -> int:
        def solve(i,j):
            if i>j:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            maxi=-maxsize
            for k in range(i,j+1):
                coins=nums[i-1]*nums[k]*nums[j+1]+solve(i,k-1)+solve(k+1,j)
                maxi=max(maxi,coins)
            dp[i][j]=maxi
            return dp[i][j]
        
        n=len(nums)
        dp=[[-1 for j in range(n+1)] for j in range(n+1)]
        nums.insert(0,1)
        nums.append(1)
        return solve(1,n)
    
#Tabulation (Bottom-Up)
#Time Complexity: O(n^3)
#Space Complexity: O(n^2)
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n=len(nums)
        nums.insert(0,1)
        nums.append(1)
        dp=[[0 for j in range(n+2)] for j in range(n+2)]
        for i in range(n,0,-1):
            for j in range(1,n+1):
                if i>j:
                    continue
                maxi=-maxsize
                for k in range(i,j+1):
                    coins=nums[i-1]*nums[k]*nums[j+1]+dp[i][k-1]+dp[k+1][j]
                    maxi=max(maxi,coins)
                dp[i][j]=maxi
        return dp[1][n]