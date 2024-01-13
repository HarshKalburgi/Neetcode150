# Permutation in String
# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.
# code

class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False
        
        s1_map = [0] * 26  # Using a fixed-size array to store the character frequencies
        window_map = [0] * 26

        for i in range(len(s1)):
            s1_map[ord(s1[i]) - ord('a')] += 1
            window_map[ord(s2[i]) - ord('a')] += 1

        for i in range(len(s2) - len(s1)):
            if s1_map == window_map:
                return True
            window_map[ord(s2[i]) - ord('a')] -= 1
            window_map[ord(s2[i + len(s1)]) - ord('a')] += 1

        return s1_map == window_map  # Checking for permutation in the last window
