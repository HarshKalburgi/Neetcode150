# Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.
# The following rules define a valid string:
# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
# code
class Solution:
    def checkValidString(self, s: str) -> bool:
        
        # store the indices of '('
        stk = []
        
        # store the indices of '*'
        star = []
        
        
        for idx, char in enumerate(s):
            
            if char == '(':
                stk.append( idx )
                
            elif char == ')':
                
                if stk:
                    stk.pop()
                elif star:
                    star.pop()
                else:
                    return False
            
            else:
                star.append( idx )
        
        
        # cancel ( and * with valid positions, i.e., '(' must be on the left hand side of '*'
        while stk and star:
            if stk[-1] > star[-1]:
                return False
        
            stk.pop()
            star.pop()
        
        
        # Accept when stack is empty, which means all braces are paired
        # Reject, otherwise.
        return len(stk) == 0
                