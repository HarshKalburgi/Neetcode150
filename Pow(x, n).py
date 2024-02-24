# Pow(x, n)
# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
# code
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0 :
            return(1)
        if n==1 :
            return(x)
        if n==-1 :
            return(1/x)
        if n%2==0 :
            a= self.myPow(x,n//2)
            return(a*a)
        else :
            a = self.myPow(x,n//2)
            return(a*a*x)