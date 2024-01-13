#  Minimum Window Substring
# Given two strings s and t of lengths m and n respectively, return the minimum window 
# substring
#  of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.
# code

class Solution(object):
    def minWindow(self, s, t):
        # Create a hashmap to store the frequency of characters in t
        t_freq = {}
        for char in t:
            if char in t_freq:
                t_freq[char] += 1
            else:
                t_freq[char] = 1

        left = 0
        required = len(t_freq)
        ans = float('inf'), None, None
        formed = 0
        window_freq = {}

        for right, char in enumerate(s):
            if char in t_freq:
                window_freq[char] = window_freq.get(char, 0) + 1
                if window_freq[char] == t_freq[char]:
                    formed += 1
            while formed == required:
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)
                if s[left] in t_freq:
                    window_freq[s[left]] -= 1
                    if window_freq[s[left]] < t_freq[s[left]]:
                        formed -= 1
                left += 1
        
        return "" if ans[0] == float('inf') else s[ans[1]:ans[2] + 1]

