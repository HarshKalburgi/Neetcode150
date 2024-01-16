# Evaluate Reverse Polish Notation
# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:

# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.
# code
class Solution:
    def evalRPN(self, tokens):
        stack = []
        operands = set(['+', '-', '*', '/'])

        for token in tokens:
            # if the token is not an operand, push it in the stack
            if token not in operands:
                stack.append(int(token))
            
            # need to perform calculation based on the operand
            else:
                b = stack.pop()
                a = stack.pop()

                if token == '+':
                    stack.append(a+b)
                elif token == '-':
                    stack.append(a-b)
                elif token == '*':
                    stack.append(a*b)
                else:
                    # true division followed by truncation towards zero
                    stack.append(int(a/b))
            
        return stack[-1]
        