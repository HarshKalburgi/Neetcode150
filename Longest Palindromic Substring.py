# Longest Palindromic Substring
# Given a string s, return the longest palindromic sub-stringn s.
# code
class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)

        res = [0, 0 ]

        def check(i, j):
            while i >= 0 and j < N:
                if s[i] == s[j]:
                    i -= 1
                    j += 1
                else:
                    return (i+1, j-1)

            return (i+1, j-1)

        max_length = [0, 0]
        cur_max = [0, 0]

        for i in range(N):
            get_odd = check(i, i)
            x, y = cur_max
            cur_dist = y - x + 1
            nX, nY = get_odd
            new_dist = nY - nX + 1
            if new_dist > cur_dist:
                cur_max = [nX, nY]
                print(cur_max)

            get_even = check(i, i+1)
            x, y = cur_max
            cur_dist = y - x + 1
            nX, nY = get_even
            new_dist = nY - nX + 1
            if new_dist > cur_dist:
                cur_max = [nX, nY]
                print(cur_max)
        
        res = cur_max
        i, j = res
        return s[i: j+ 1]