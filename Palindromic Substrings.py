# Palindromic Substrings
# Given a string s, return the number of palindromic substrings in it.
# A string is a palindrome when it reads the same backward as forward.
# A substring is a contiguous sequence of characters within the string.
# code

class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        TC - O(N*N)
        SC - O(1)
        """
        n = len(s)
        res = 0

        for i in range(n):
            # odd case
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                res +=1
                l -=1
                r +=1
            
            # even case
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                res +=1
                l -=1
                r +=1
        return res