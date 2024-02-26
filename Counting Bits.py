# Counting Bits
# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

# code
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]

        for number in range(1, n + 1):
            ans.append(ans[number >> 1] + number % 2)

        return ans
        