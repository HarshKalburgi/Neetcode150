# Best Time to Buy and Sell Stock with Cooldown

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

# After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

# code
class Solution:
    # def dp(self,i,buy,prices,n,dct):
    #     if i>=n:
    #         return 0
    #     if (i,buy) in dct:
    #         return dct[(i,buy)]
    #     if buy:
    #         x=max(self.dp(i+1,buy,prices,n,dct),self.dp(i+1,0,prices,n,dct)-prices[i])
    #     else:
    #         x=max(self.dp(i+1,buy,prices,n,dct),self.dp(i+2,1,prices,n,dct)+prices[i])
    #     dct[(i,buy)]=x
    #     return x

    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        # dp=[[0]*2 for i in range(n+2)]
        ahd=[0]*2
        ahd2=[0]*2
        for i in range(n-1,-1,-1):
            curr=[0]*2
            for buy in range(2):
                if buy:
                    curr[buy]=max(ahd[buy],ahd[0]-prices[i])
                else:
                    curr[buy]=max(ahd[buy],ahd2[1]+prices[i])
            ahd2=ahd[:]
            ahd=curr[:]
        return ahd[1]