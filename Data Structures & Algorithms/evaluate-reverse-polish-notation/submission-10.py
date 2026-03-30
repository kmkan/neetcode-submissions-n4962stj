import operator
import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
        stack = []
        for t in tokens:
            if t in operators:
                right = stack.pop()
                left = stack.pop()
                stack.append(math.trunc(operators[t](left, right)))
            else:
                stack.append(int(t))
            print(stack)
        print(stack)
        return stack[-1]