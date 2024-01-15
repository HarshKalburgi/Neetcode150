#  Generate Parentheses
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# code
class Solution(object):
    def generateParenthesis(self, n):
        def backtrack(s, left, right, res=[]):
            if len(s) == 2 * n:
                res.append(s)
                return
            if left < n:
                backtrack(s + '(', left + 1, right)
            if right < left:
                backtrack(s + ')', left, right + 1)
            return res

        return backtrack('', 0, 0)

